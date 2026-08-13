# pip install keyboard
import keyboard  # using module keyboard
# pip install opencv-python
import cv2 #computer vision library
import time


           # 1. Configuration Settings
VIDEO_PATH = "video1560309659.mp4"  
NOTES_FILE = "video_notes.txt"

def save_note(timestamp_ms, text):
    """Saves the note with a formatted timestamp to a text file."""
    seconds = int((timestamp_ms / 1000) % 60)
    minutes = int((timestamp_ms / (1000 * 60)) % 60)
    hours = int((timestamp_ms / (1000 * 60 * 60)) % 24)
    time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    
    with open(NOTES_FILE, "a") as f:
        f.write(f"[{time_str}] - {text}\n")
    print(f"Saved Note at {time_str}: {text}")

def main():
    # Initialize video capture stream
    cap = cv2.VideoCapture(VIDEO_PATH)
    if not cap.isOpened():
        print("Error: Could not open video source.")
        return

    # Window setup
    window_name = "OpenCV Video Notetaker"
    cv2.namedWindow(window_name)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("End of video stream or cannot read frame.")
            break

        # Display instructions directly on the running video frame
        display_frame = frame.copy()
        cv2.putText(display_frame, "Press Q to quit", 
                    (15, 30), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.6, (0, 255, 0), 2)
        
        cv2.imshow(window_name, display_frame)
        
        # Monitor user keystrokes
        key = cv2.waitKey(25) & 0xFF
        
        # Case A: User quits
        if key == ord('q'):
            break
            
        # Case B: User pauses video to write a note
        elif key == ord('1'):
            current_time_ms = cap.get(cv2.CAP_PROP_POS_MSEC)
            note_text = "Touches trash can"
            save_note(current_time_ms, note_text)

        elif key == ord('2'):
            current_time_ms = cap.get(cv2.CAP_PROP_POS_MSEC)
            note_text = "Confusion over step"
            save_note(current_time_ms, note_text)

        elif key == ord(' '):
            current_time_ms = cap.get(cv2.CAP_PROP_POS_MSEC)
            notetext = ""    
            while True:
                # Create an overlay overlay on the paused frame for text entry
                paused_frame = frame.copy()
                
                # Darken background slightly to emphasize text field
                overlay = paused_frame.copy()
                cv2.rectangle(overlay, (0, 0), (paused_frame.shape[1], 110), (0, 0, 0), -1)
                cv2.addWeighted(overlay, 0.6, paused_frame, 0.4, 0, paused_frame)
                
                # Render text interface
                cv2.putText(paused_frame, "TYPE NOTE & PRESS ENTER TO SAVE:", 
                            (15, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
                cv2.putText(paused_frame, f"> {notetext}_", 
                            (15, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                
                cv2.imshow(window_name, paused_frame)
                
                # Capture character codes character-by-character
                input_key = cv2.waitKey(0) & 0xFF
                
                # Finish writing note
                if input_key == 13:  # Enter Key
                    if notetext.strip():
                        save_note(current_time_ms, notetext)
                    break
                # Handle backspaces
                elif input_key == 8 or input_key == 255:  # Backspace keys
                    notetext = notetext[:-1]
                # Filter printable ASCII characters
                elif 32 <= input_key <= 126:
                    notetext += chr(input_key)

    # Cleanup resources properly
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
