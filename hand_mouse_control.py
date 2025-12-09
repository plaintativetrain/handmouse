import cv2
import numpy as np
import pyautogui
import mediapipe as mp
from math import hypot
import time
import threading

# Configure PyAutoGUI for macOS compatibility
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.0  # Minimize delay between actions

# Get screen dimensions
screen_width, screen_height = pyautogui.size()

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Hand detection configuration
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
    model_complexity=1
)

# Initialize webcam
cap = cv2.VideoCapture(0)

# Set webcam resolution (lower resolution for better performance)
cam_width = 640
cam_height = 480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, cam_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, cam_height)
cap.set(cv2.CAP_PROP_FPS, 60)  # Request higher frame rate

# Screen edge padding (reduce the mapping area for easier edge access)
# This means you only need to move your hand 70% of the way to reach screen edges
edge_padding = 0.15  # 15% padding on each side

# Click detection thresholds
base_click_threshold = 0.19  # Base threshold ratio for adaptive detection
scroll_threshold = 0.005  # Threshold for detecting scroll movement
scroll_sensitivity = 0.05  # Scroll speed multiplier

# State variables to track click states (for holding)
left_click_held = False
right_click_held = False
previous_y = None  # For scroll tracking

def calculate_distance(point1, point2):
    """Calculate Euclidean distance between two points"""
    return hypot(point1[0] - point2[0], point1[1] - point2[1])

def get_landmark_distance(landmark1, landmark2):
    """Calculate normalized distance between two MediaPipe landmarks"""
    x1, y1 = landmark1.x, landmark1.y
    x2, y2 = landmark2.x, landmark2.y
    distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

# Movement Thread for smoother cursor movement with jitter reduction
class CursorMovementThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.daemon = True
        self.current_x, self.current_y = pyautogui.position()
        self.target_x, self.target_y = self.current_x, self.current_y
        self.running = True
        self.active = False
        self.jitter_threshold = 0.003  # Ignore tiny movements
    
    def run(self):
        while self.running:
            if self.active:
                distance = np.hypot(self.target_x - self.current_x, 
                                   self.target_y - self.current_y)
                screen_diagonal = np.hypot(screen_width, screen_height)
                
                # Only move if distance is above jitter threshold
                if distance / screen_diagonal > self.jitter_threshold:
                    step = max(0.0001, distance / 12)  # Smoother movement
                    if distance != 0:
                        step_x = (self.target_x - self.current_x) / distance * step
                        step_y = (self.target_y - self.current_y) / distance * step
                        self.current_x += step_x
                        self.current_y += step_y
                        try:
                            pyautogui.moveTo(self.current_x, self.current_y)
                        except Exception as e:
                            print(f"Mouse move error: {e}")
                time.sleep(0.001)
            else:
                time.sleep(0.1)
    
    def update_target(self, x, y):
        self.target_x, self.target_y = x, y
    
    def activate(self):
        self.active = True
    
    def deactivate(self):
        self.active = False
    
    def stop(self):
        self.running = False

# Scrolling Thread for smooth scrolling with inertia
class ScrollThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.daemon = True
        self.scroll_queue = []
        self.scroll_lock = threading.Lock()
        self.running = True
        self.inertia = 0.95  # Slower reduction for rolling stop effect
        self.scroll_step = 0.01  # Smaller step for smoother scroll
        self.inertia_threshold = 0.01  # Minimum inertia scroll amount
    
    def run(self):
        while self.running:
            if self.scroll_queue:
                with self.scroll_lock:
                    scroll_amount = self.scroll_queue.pop(0)
                try:
                    pyautogui.scroll(int(scroll_amount))
                except Exception as e:
                    print(f"Scroll error: {e}")
                
                # Apply inertia for smooth rolling effect
                if abs(scroll_amount) > self.inertia_threshold:
                    scroll_amount *= self.inertia
                    if abs(scroll_amount) > self.scroll_step:
                        with self.scroll_lock:
                            self.scroll_queue.append(scroll_amount)
            time.sleep(0.005)  # Increased frequency for smoother processing
    
    def add_scroll(self, scroll_amount):
        with self.scroll_lock:
            self.scroll_queue.append(scroll_amount)
    
    def stop(self):
        self.running = False

def map_coordinates(x, y, cam_w, cam_h, screen_w, screen_h):
    """Map hand coordinates from webcam to screen coordinates with mirroring and reduced scaling"""
    # Apply padding to reduce the mapping area
    # This allows reaching screen edges with less hand movement
    padding_w = cam_w * edge_padding
    padding_h = cam_h * edge_padding
    
    # Map with padding (hand only needs to reach 15% from edge to hit screen edge)
    screen_x = np.interp(x, [padding_w, cam_w - padding_w], [0, screen_w])
    screen_y = np.interp(y, [padding_h, cam_h - padding_h], [0, screen_h])
    
    # Clamp to screen boundaries
    screen_x = max(0, min(screen_w, screen_x))
    screen_y = max(0, min(screen_h, screen_y))
    
    return int(screen_x), int(screen_y)

# Initialize the movement and scroll threads
movement_thread = CursorMovementThread()
scroll_thread = ScrollThread()
movement_thread.start()
scroll_thread.start()

print("HandMouse - Gesture Control Started!")
print("=" * 60)
print("IMPORTANT - macOS Users:")
print("If you see permission errors, grant Accessibility access:")
print("System Preferences > Security & Privacy > Privacy > Accessibility")
print("Add Terminal (or your IDE) to the allowed apps list")
print("=" * 60)
print("\nControls:")
print("- Move your hand to control the mouse (tracks ring finger base)")
print("- HOLD index finger + thumb pinched for LEFT CLICK (drag/select text)")
print("- Pinch middle finger + thumb for RIGHT CLICK")
print("- Pinch ring finger + thumb and move up/down to SCROLL")
print("- Press 'q' or ESC to quit")
print("\nStarting in 2 seconds...")
time.sleep(2)
print()

try:
    while True:
        # Read a frame from the webcam
        success, frame = cap.read()
        if not success:
            print("Failed to read from webcam")
            break
        
        # Flip frame horizontally for mirror effect
        frame = cv2.flip(frame, 1)
        
        # Convert BGR to RGB for MediaPipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Mark frame as not writeable for performance
        rgb_frame.flags.writeable = False
        
        # Process the frame to detect hands
        results = hands.process(rgb_frame)
        
        # Mark frame as writeable again
        rgb_frame.flags.writeable = True
        frame = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2BGR)
        
        # Check for the presence of hands
        if results.multi_hand_landmarks:
            movement_thread.activate()
            
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw hand landmarks on the frame
                mp_drawing.draw_landmarks(
                    frame, 
                    hand_landmarks, 
                    mp_hands.HAND_CONNECTIONS
                )
                
                # Get landmark coordinates
                landmarks = hand_landmarks.landmark
                
                # Use RING_FINGER_MCP (base of ring finger, landmark 14) for tracking
                # This is more stable than finger tips and doesn't move during clicks
                ring_finger_mcp = landmarks[mp_hands.HandLandmark.RING_FINGER_MCP]
                mcp_x = int(ring_finger_mcp.x * cam_width)
                mcp_y = int(ring_finger_mcp.y * cam_height)
                
                # Convert video coordinates to screen coordinates
                target_x, target_y = map_coordinates(
                    mcp_x, mcp_y,
                    cam_width, cam_height,
                    screen_width, screen_height
                )
                
                # Update target position in movement thread
                movement_thread.update_target(target_x, target_y)
                
                # Calculate adaptive touch threshold based on hand size
                wrist = landmarks[mp_hands.HandLandmark.WRIST]
                middle_finger_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
                hand_size = get_landmark_distance(wrist, middle_finger_tip)
                adaptive_threshold = base_click_threshold * hand_size
                
                # Get finger tip landmarks
                index_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]
                middle_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
                ring_tip = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP]
                
                # Calculate distances for gesture detection
                index_thumb_distance = get_landmark_distance(index_tip, thumb_tip)
                middle_thumb_distance = get_landmark_distance(middle_tip, thumb_tip)
                ring_thumb_distance = get_landmark_distance(ring_tip, thumb_tip)
                
                # LEFT CLICK: Index finger + thumb pinch - HOLD while pinched
                if index_thumb_distance < adaptive_threshold:
                    if not left_click_held:
                        try:
                            pyautogui.mouseDown()
                            left_click_held = True
                        except Exception as e:
                            print(f"Mouse down error: {e}")
                    cv2.putText(frame, "LEFT CLICK HELD", (10, 70), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                else:
                    if left_click_held:
                        try:
                            pyautogui.mouseUp()
                            left_click_held = False
                        except Exception as e:
                            print(f"Mouse up error: {e}")
                
                # RIGHT CLICK: Middle finger + thumb pinch (NOT index)
                if middle_thumb_distance < adaptive_threshold:
                    if not right_click_held:
                        try:
                            pyautogui.rightClick()
                            right_click_held = True
                        except Exception as e:
                            print(f"Right click error: {e}")
                    cv2.putText(frame, "RIGHT CLICK", (10, 100), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                else:
                    if right_click_held:
                        right_click_held = False
                
                # SCROLL: Ring finger + thumb pinch and move up/down
                if ring_thumb_distance < adaptive_threshold:
                    # Scroll gesture detection
                    if previous_y is not None:
                        delta_y = ring_tip.y - previous_y
                        if abs(delta_y) > scroll_threshold:
                            scroll_amount = delta_y * screen_height * scroll_sensitivity
                            scroll_thread.add_scroll(scroll_amount)
                    previous_y = ring_tip.y
                    cv2.putText(frame, "SCROLLING", (10, 130), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)
                else:
                    previous_y = None
                
                # Draw circles on fingertips for visualization
                index_x = int(index_tip.x * cam_width)
                index_y = int(index_tip.y * cam_height)
                thumb_x = int(thumb_tip.x * cam_width)
                thumb_y = int(thumb_tip.y * cam_height)
                middle_x = int(middle_tip.x * cam_width)
                middle_y = int(middle_tip.y * cam_height)
                ring_x = int(ring_tip.x * cam_width)
                ring_y = int(ring_tip.y * cam_height)
                
                cv2.circle(frame, (index_x, index_y), 8, (255, 0, 0), -1)  # Blue - index
                cv2.circle(frame, (thumb_x, thumb_y), 8, (0, 255, 0), -1)  # Green - thumb
                cv2.circle(frame, (middle_x, middle_y), 8, (0, 0, 255), -1)  # Red - middle
                cv2.circle(frame, (ring_x, ring_y), 8, (255, 0, 255), -1)  # Magenta - ring
                cv2.circle(frame, (mcp_x, mcp_y), 10, (255, 255, 0), 2)  # Yellow - tracking point
                
                # Display distances for debugging
                cv2.putText(frame, f"I-T: {index_thumb_distance:.3f}", (10, 30), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
                cv2.putText(frame, f"M-T: {middle_thumb_distance:.3f}", (10, 50), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        else:
            # No hands detected - release any held buttons
            if left_click_held:
                try:
                    pyautogui.mouseUp()
                    left_click_held = False
                except Exception as e:
                    print(f"Mouse up error: {e}")
            movement_thread.deactivate()
        
        # Add instructions at bottom of frame
        frame_height = frame.shape[0]
        cv2.putText(frame, "Press 'Q' or ESC to quit", (10, frame_height - 10), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        
        # Display the frame
        cv2.imshow('HandMouse - Gesture Control', frame)
        
        # Press 'q' or 'ESC' to quit
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q') or key == 27:
            break

finally:
    # Cleanup
    movement_thread.stop()
    scroll_thread.stop()
    cap.release()
    cv2.destroyAllWindows()
    hands.close()
    print("\nHandMouse stopped.")
