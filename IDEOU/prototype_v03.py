import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import json
import os
import threading
import time

class ElderLifeConnect:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ElderLife Connect")
        self.root.geometry("1000x700")
        
        # Enhanced color palette - calming and accessible
        self.colors = {
            'bg_primary': '#f8f9fa',      # Very light gray-blue
            'bg_secondary': '#ffffff',     # Pure white
            'accent_blue': '#5a9fd4',      # Soft blue
            'accent_green': '#6ab04c',     # Gentle green
            'accent_orange': '#f0932b',    # Warm orange
            'text_primary': '#2c3e50',     # Dark blue-gray
            'text_secondary': '#34495e',   # Medium blue-gray
            'border': '#e1e8ed',          # Light border
            'shadow': '#ddd'              # Soft shadow
        }
        
        self.root.configure(bg=self.colors['bg_primary'])
        
        # Data storage
        self.user_data = self.load_user_data()
        self.medications = self.user_data.get('medications', [])
        self.health_records = self.user_data.get('health_records', [])
        self.appointments = self.user_data.get('appointments', [])
        
        # Voice control simulation
        self.voice_enabled = True
        self.listening = False
        
        # Configure enhanced styles
        self.setup_enhanced_styles()
        
        # Initialize main interface
        self.create_main_interface()
        
        # Start voice control simulation
        self.start_voice_simulation()
        
    def setup_enhanced_styles(self):
        """Configure enhanced styles for maximum accessibility"""
        try:
            style = ttk.Style()
            
            # Extra large buttons with high contrast
            style.configure('XLarge.TButton', 
                          font=('Arial', 18, 'bold'), 
                          padding=(20, 15),
                          relief='flat')
            
            # Large header text
            style.configure('XLHeader.TLabel', 
                          font=('Arial', 24, 'bold'), 
                          background=self.colors['bg_primary'],
                          foreground=self.colors['text_primary'])
            
            # Medium header
            style.configure('MedHeader.TLabel', 
                          font=('Arial', 20, 'bold'), 
                          background=self.colors['bg_primary'],
                          foreground=self.colors['text_primary'])
            
            # Large info text
            style.configure('XLInfo.TLabel', 
                          font=('Arial', 16), 
                          background=self.colors['bg_primary'],
                          foreground=self.colors['text_secondary'])
            
        except Exception as e:
            print(f"Style configuration warning: {e}")
        
    def load_user_data(self):
        """Load user data from file or create default"""
        if os.path.exists('elderlife_data.json'):
            try:
                with open('elderlife_data.json', 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error loading data: {e}")
        
        # Default data with fewer initial items for simplicity
        return {
            'medications': [
                {
                    'name': 'Morning Medicine',
                    'dosage': '10mg',
                    'schedule': ['08:00'],
                    'taken_today': {'08:00': False}
                }
            ],
            'health_records': [],
            'appointments': [
                {
                    'date': '2025-06-05',
                    'time': '10:00',
                    'doctor': 'Dr. Smith',
                    'type': 'Check-up'
                }
            ]
        }
    
    def save_user_data(self):
        """Save user data to file"""
        try:
            data_to_save = {
                'medications': self.medications,
                'health_records': self.health_records,
                'appointments': self.appointments
            }
            with open('elderlife_data.json', 'w') as f:
                json.dump(data_to_save, f, indent=2)
        except Exception as e:
            print(f"Error saving data: {e}")
            messagebox.showerror("Save Error", f"Could not save data: {str(e)}")
    
    def create_enhanced_button(self, parent, text, command, bg_color, width=25, height=3):
        """Create an enhanced, accessible button"""
        button = tk.Button(
            parent, 
            text=text, 
            command=command,
            font=('Arial', 18, 'bold'),
            width=width, 
            height=height,
            bg=bg_color,
            fg='white',
            relief='flat',
            bd=0,
            activebackground=self.darken_color(bg_color),
            activeforeground='white',
            cursor='hand2'
        )
        
        # Add subtle shadow effect
        shadow_frame = tk.Frame(parent, bg=self.colors['shadow'], height=2)
        shadow_frame.pack(fill='x', padx=22, pady=(0, 5))
        
        return button
    
    def darken_color(self, hex_color):
        """Darken a hex color for hover effects"""
        # Simple darkening by reducing each RGB component
        hex_color = hex_color.lstrip('#')
        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        darkened = tuple(max(0, c - 30) for c in rgb)
        return '#{:02x}{:02x}{:02x}'.format(*darkened)
    
    def create_main_interface(self):
        """Create the simplified main dashboard interface"""
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()
            
        # Main container with generous padding
        main_container = tk.Frame(self.root, bg=self.colors['bg_primary'])
        main_container.pack(fill='both', expand=True, padx=40, pady=30)
        
        # Voice control indicator
        voice_frame = tk.Frame(main_container, bg=self.colors['bg_primary'])
        voice_frame.pack(fill='x', pady=(0, 20))
        
        voice_status = "🎤 Voice Control: ON" if self.voice_enabled else "🎤 Voice Control: OFF"
        voice_color = self.colors['accent_green'] if self.voice_enabled else self.colors['text_secondary']
        
        self.voice_label = tk.Label(
            voice_frame, 
            text=voice_status,
            font=('Arial', 14, 'bold'),
            bg=self.colors['bg_primary'],
            fg=voice_color
        )
        self.voice_label.pack(anchor='ne')
        
        # Main title with better spacing
        title_frame = tk.Frame(main_container, bg=self.colors['bg_primary'])
        title_frame.pack(pady=(0, 30))
        
        title_label = tk.Label(
            title_frame, 
            text="ElderLife Connect",
            font=('Arial', 28, 'bold'),
            bg=self.colors['bg_primary'],
            fg=self.colors['text_primary']
        )
        title_label.pack()
        
        # Current time with better visibility
        time_text = datetime.now().strftime('%A, %B %d, %Y')
        time_label = tk.Label(
            title_frame, 
            text=time_text,
            font=('Arial', 18),
            bg=self.colors['bg_primary'],
            fg=self.colors['text_secondary']
        )
        time_label.pack(pady=(10, 0))
        
        # Simplified main menu - only 3 primary actions
        button_container = tk.Frame(main_container, bg=self.colors['bg_primary'])
        button_container.pack(expand=True)
        
        # Primary buttons with extra spacing and color coding
        primary_buttons = [
            ("💊 My Medicine", self.show_medications, self.colors['accent_blue']),
            ("👨‍⚕️ Doctor Visit", self.show_appointments, self.colors['accent_green']),
            ("🆘 Get Help", self.emergency_help, self.colors['accent_orange'])
        ]
        
        for text, command, color in primary_buttons:
            btn = self.create_enhanced_button(button_container, text, command, color)
            btn.pack(pady=15)
        
        # Secondary actions in smaller, less prominent buttons
        secondary_frame = tk.Frame(main_container, bg=self.colors['bg_primary'])
        secondary_frame.pack(pady=(30, 0))
        
        secondary_buttons = [
            ("📊 Health Records", self.show_health_tracking),
            ("⚙️ Settings", self.show_settings)
        ]
        
        for text, command in secondary_buttons:
            btn = tk.Button(
                secondary_frame, 
                text=text, 
                command=command,
                font=('Arial', 14),
                width=20, 
                height=1,
                bg=self.colors['bg_secondary'],
                fg=self.colors['text_primary'],
                relief='solid',
                bd=1,
                cursor='hand2'
            )
            btn.pack(side='left', padx=10)
        
        # Check for medication reminders
        self.check_medication_reminders()
    
    def start_voice_simulation(self):
        """Start voice control simulation in background"""
        def voice_worker():
            while True:
                try:
                    time.sleep(10)  # Check every 10 seconds
                    if self.voice_enabled and hasattr(self, 'voice_label'):
                        # Simulate voice command detection
                        if not self.listening:
                            self.simulate_voice_listening()
                except:
                    break
        
        voice_thread = threading.Thread(target=voice_worker, daemon=True)
        voice_thread.start()
    
    def simulate_voice_listening(self):
        """Simulate voice command listening"""
        self.listening = True
        if hasattr(self, 'voice_label'):
            self.voice_label.config(text="🎤 Listening...", fg=self.colors['accent_orange'])
            
        # Simulate processing time
        self.root.after(2000, self.voice_processing_complete)
    
    def voice_processing_complete(self):
        """Complete voice processing simulation"""
        self.listening = False
        if hasattr(self, 'voice_label'):
            self.voice_label.config(text="🎤 Voice Control: ON", fg=self.colors['accent_green'])
        
        # Occasionally show voice command result
        import random
        if random.random() < 0.3:  # 30% chance
            commands = [
                "Voice command: 'Show my medicine'",
                "Voice command: 'When is my appointment?'",
                "Voice command: 'Call for help'"
            ]
            selected_command = random.choice(commands)
            messagebox.showinfo("Voice Command Detected", 
                              f"🎤 {selected_command}\n\n" +
                              "Say 'Yes' to execute or 'Cancel' to ignore.")
    
    def show_medications(self):
        """Display simplified medication management interface"""
        try:
            # Clear window
            for widget in self.root.winfo_children():
                widget.destroy()
                
            # Main container
            main_container = tk.Frame(self.root, bg=self.colors['bg_primary'])
            main_container.pack(fill='both', expand=True, padx=40, pady=30)
            
            # Header with large back button
            header_frame = tk.Frame(main_container, bg=self.colors['bg_primary'])
            header_frame.pack(fill='x', pady=(0, 30))
            
            back_btn = tk.Button(
                header_frame, 
                text="← Back Home", 
                command=self.create_main_interface,
                font=('Arial', 16, 'bold'), 
                bg=self.colors['text_secondary'], 
                fg='white',
                width=15,
                height=2,
                relief='flat',
                cursor='hand2'
            )
            back_btn.pack(side='left')
            
            title_label = tk.Label(
                header_frame, 
                text="💊 My Medicine",
                font=('Arial', 24, 'bold'),
                bg=self.colors['bg_primary'],
                fg=self.colors['text_primary']
            )
            title_label.pack(side='right')
            
            # Medication cards with enhanced spacing and contrast
            if not self.medications:
                no_med_frame = tk.Frame(main_container, bg=self.colors['bg_secondary'], 
                                       relief='solid', bd=2)
                no_med_frame.pack(fill='both', expand=True, pady=20)
                
                no_med_label = tk.Label(
                    no_med_frame, 
                    text="No medications set up yet",
                    font=('Arial', 18),
                    bg=self.colors['bg_secondary'],
                    fg=self.colors['text_secondary']
                )
                no_med_label.pack(expand=True)
                return
            
            for i, med in enumerate(self.medications):
                # Enhanced medication card
                card_frame = tk.Frame(main_container, bg=self.colors['bg_secondary'], 
                                    relief='solid', bd=2)
                card_frame.pack(fill='x', pady=15)
                
                # Card content with generous padding
                content_frame = tk.Frame(card_frame, bg=self.colors['bg_secondary'])
                content_frame.pack(fill='both', padx=30, pady=25)
                
                # Medicine name - very prominent
                name_label = tk.Label(
                    content_frame, 
                    text=med['name'],
                    font=('Arial', 22, 'bold'),
                    bg=self.colors['bg_secondary'],
                    fg=self.colors['text_primary']
                )
                name_label.pack(anchor='w', pady=(0, 10))
                
                # Dosage information
                dosage_label = tk.Label(
                    content_frame, 
                    text=f"Amount: {med['dosage']}",
                    font=('Arial', 16),
                    bg=self.colors['bg_secondary'],
                    fg=self.colors['text_secondary']
                )
                dosage_label.pack(anchor='w', pady=(0, 15))
                
                # Schedule with clear status
                for time_slot in med['schedule']:
                    schedule_frame = tk.Frame(content_frame, bg=self.colors['bg_secondary'])
                    schedule_frame.pack(fill='x', pady=5)
                    
                    time_label = tk.Label(
                        schedule_frame, 
                        text=f"Time: {time_slot}",
                        font=('Arial', 18, 'bold'),
                        bg=self.colors['bg_secondary'],
                        fg=self.colors['text_primary']
                    )
                    time_label.pack(side='left')
                    
                    taken = med['taken_today'].get(time_slot, False)
                    
                    if taken:
                        status_label = tk.Label(
                            schedule_frame, 
                            text="✅ TAKEN",
                            font=('Arial', 16, 'bold'),
                            fg=self.colors['accent_green'],
                            bg=self.colors['bg_secondary']
                        )
                        status_label.pack(side='right')
                    else:
                        take_btn = tk.Button(
                            schedule_frame, 
                            text="✓ Take Now", 
                            command=lambda m=i, t=time_slot: self.mark_medication_taken(m, t),
                            font=('Arial', 16, 'bold'), 
                            bg=self.colors['accent_blue'], 
                            fg='white',
                            width=12,
                            height=2,
                            relief='flat',
                            cursor='hand2'
                        )
                        take_btn.pack(side='right')
                        
        except Exception as e:
            messagebox.showerror("Error", f"Error displaying medications: {str(e)}")
            self.create_main_interface()
    
    def mark_medication_taken(self, med_index, time_slot):
        """Mark medication as taken with enhanced feedback"""
        try:
            if med_index < len(self.medications):
                self.medications[med_index]['taken_today'][time_slot] = True
                self.save_user_data()
                
                # Enhanced confirmation dialog
                messagebox.showinfo(
                    "Medicine Taken!", 
                    f"✅ Great job!\n\n" +
                    f"{self.medications[med_index]['name']}\n" +
                    f"has been marked as taken.\n\n" +
                    f"Time: {time_slot}"
                )
                self.show_medications()  # Refresh the view
        except Exception as e:
            messagebox.showerror("Error", f"Error marking medication: {str(e)}")
    
    def show_appointments(self):
        """Display simplified appointments interface"""
        try:
            # Clear window
            for widget in self.root.winfo_children():
                widget.destroy()
                
            # Main container
            main_container = tk.Frame(self.root, bg=self.colors['bg_primary'])
            main_container.pack(fill='both', expand=True, padx=40, pady=30)
            
            # Header
            header_frame = tk.Frame(main_container, bg=self.colors['bg_primary'])
            header_frame.pack(fill='x', pady=(0, 30))
            
            back_btn = tk.Button(
                header_frame, 
                text="← Back Home", 
                command=self.create_main_interface,
                font=('Arial', 16, 'bold'), 
                bg=self.colors['text_secondary'], 
                fg='white',
                width=15,
                height=2,
                relief='flat',
                cursor='hand2'
            )
            back_btn.pack(side='left')
            
            title_label = tk.Label(
                header_frame, 
                text="👨‍⚕️ Doctor Visits",
                font=('Arial', 24, 'bold'),
                bg=self.colors['bg_primary'],
                fg=self.colors['text_primary']
            )
            title_label.pack(side='right')
            
            # Appointments with enhanced visibility
            if not self.appointments:
                no_apt_frame = tk.Frame(main_container, bg=self.colors['bg_secondary'], 
                                       relief='solid', bd=2)
                no_apt_frame.pack(fill='both', expand=True, pady=20)
                
                tk.Label(
                    no_apt_frame, 
                    text="No upcoming appointments",
                    font=('Arial', 18),
                    bg=self.colors['bg_secondary'],
                    fg=self.colors['text_secondary']
                ).pack(expand=True)
            else:
                for apt in self.appointments:
                    # Enhanced appointment card
                    card_frame = tk.Frame(main_container, bg=self.colors['bg_secondary'], 
                                        relief='solid', bd=2)
                    card_frame.pack(fill='x', pady=15)
                    
                    content_frame = tk.Frame(card_frame, bg=self.colors['bg_secondary'])
                    content_frame.pack(fill='both', padx=30, pady=25)
                    
                    # Date and time - very prominent
                    datetime_label = tk.Label(
                        content_frame, 
                        text=f"📅 {apt['date']} at {apt['time']}",
                        font=('Arial', 20, 'bold'),
                        bg=self.colors['bg_secondary'],
                        fg=self.colors['text_primary']
                    )
                    datetime_label.pack(anchor='w', pady=(0, 10))
                    
                    # Doctor name
                    doctor_label = tk.Label(
                        content_frame, 
                        text=f"Doctor: {apt['doctor']}",
                        font=('Arial', 16),
                        bg=self.colors['bg_secondary'],
                        fg=self.colors['text_secondary']
                    )
                    doctor_label.pack(anchor='w', pady=(0, 5))
                    
                    # Appointment type
                    type_label = tk.Label(
                        content_frame, 
                        text=f"Visit Type: {apt['type']}",
                        font=('Arial', 16),
                        bg=self.colors['bg_secondary'],
                        fg=self.colors['text_secondary']
                    )
                    type_label.pack(anchor='w')
            
            # Video call button - more prominent
            video_btn = self.create_enhanced_button(
                main_container, 
                "📹 Start Video Call", 
                self.start_telehealth,
                self.colors['accent_green'],
                width=20,
                height=2
            )
            video_btn.pack(pady=30)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error displaying appointments: {str(e)}")
            self.create_main_interface()
    
    def start_telehealth(self):
        """Enhanced telehealth session simulation"""
        messagebox.showinfo(
            "Video Call Starting", 
            "📹 Connecting to your doctor...\n\n" +
            "Please wait while we:\n" +
            "• Test your camera and microphone\n" +
            "• Connect to Dr. Smith\n" +
            "• Prepare your health information\n\n" +
            "This may take a moment."
        )
    
    def emergency_help(self):
        """Enhanced emergency help interface"""
        try:
            # Create custom emergency dialog
            emergency_window = tk.Toplevel(self.root)
            emergency_window.title("Emergency Help")
            emergency_window.geometry("600x400")
            emergency_window.configure(bg=self.colors['accent_orange'])
            emergency_window.grab_set()  # Make it modal
            
            # Center the window
            emergency_window.transient(self.root)
            
            # Emergency content
            content_frame = tk.Frame(emergency_window, bg=self.colors['accent_orange'])
            content_frame.pack(fill='both', expand=True, padx=30, pady=30)
            
            # Large emergency title
            title_label = tk.Label(
                content_frame,
                text="🆘 EMERGENCY HELP",
                font=('Arial', 28, 'bold'),
                bg=self.colors['accent_orange'],
                fg='white'
            )
            title_label.pack(pady=(0, 30))
            
            # Question
            question_label = tk.Label(
                content_frame,
                text="Do you need immediate medical help?",
                font=('Arial', 18),
                bg=self.colors['accent_orange'],
                fg='white'
            )
            question_label.pack(pady=(0, 30))
            
            # Large buttons
            button_frame = tk.Frame(content_frame, bg=self.colors['accent_orange'])
            button_frame.pack()
            
            yes_btn = tk.Button(
                button_frame,
                text="YES - Call 911",
                command=lambda: self.call_emergency(emergency_window),
                font=('Arial', 16, 'bold'),
                bg='red',
                fg='white',
                width=15,
                height=3,
                relief='flat',
                cursor='hand2'
            )
            yes_btn.pack(side='left', padx=10)
            
            no_btn = tk.Button(
                button_frame,
                text="NO - Other Help",
                command=lambda: self.show_other_help(emergency_window),
                font=('Arial', 16, 'bold'),
                bg=self.colors['accent_blue'],
                fg='white',
                width=15,
                height=3,
                relief='flat',
                cursor='hand2'
            )
            no_btn.pack(side='left', padx=10)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error in emergency help: {str(e)}")
    
    def call_emergency(self, window):
        """Simulate emergency call"""
        window.destroy()
        messagebox.showwarning(
            "Emergency Services", 
            "🚨 CALLING 911 NOW 🚨\n\n" +
            "Your location has been shared\n" +
            "Medical information sent\n" +
            "Help is on the way!\n\n" +
            "Stay on the line with the operator."
        )
    
    def show_other_help(self, window):
        """Show non-emergency help options"""
        window.destroy()
        messagebox.showinfo(
            "Help Contacts", 
            "📞 Here are your help contacts:\n\n" +
            "🏥 Doctor: (555) 123-4567\n" +
            "👨‍👩‍👧‍👦 Family: (555) 987-6543\n" +
            "💊 Pharmacy: (555) 246-8135\n" +
            "🏥 Hospital: (555) 911-1000\n\n" +
            "Tap any number to call"
        )
    
    def show_health_tracking(self):
        """Simplified health tracking interface"""
        # This method can be simplified further based on the same principles
        messagebox.showinfo("Health Records", "📊 Health tracking feature\ncoming soon!")
    
    def show_settings(self):
        """Simplified settings interface"""
        messagebox.showinfo("Settings", "⚙️ Settings panel\ncoming soon!")
    
    def check_medication_reminders(self):
        """Enhanced medication reminder system"""
        try:
            current_time = datetime.now().strftime('%H:%M')
            
            for med in self.medications:
                for time_slot in med['schedule']:
                    if (time_slot == current_time and 
                        not med['taken_today'].get(time_slot, False)):
                        
                        # Create prominent reminder window
                        reminder_window = tk.Toplevel(self.root)
                        reminder_window.title("Medicine Reminder")
                        reminder_window.geometry("500x300")
                        reminder_window.configure(bg=self.colors['accent_blue'])
                        reminder_window.grab_set()
                        
                        content_frame = tk.Frame(reminder_window, bg=self.colors['accent_blue'])
                        content_frame.pack(fill='both', expand=True, padx=20, pady=20)
                        
                        tk.Label(
                            content_frame,
                            text="⏰ MEDICINE TIME!",
                            font=('Arial', 24, 'bold'),
                            bg=self.colors['accent_blue'],
                            fg='white'
                        ).pack(pady=(0, 20))
                        
                        tk.Label(
                            content_frame,
                            text=f"💊 {med['name']}\n{med['dosage']}",
                            font=('Arial', 18),
                            bg=self.colors['accent_blue'],
                            fg='white'
                        ).pack(pady=(0, 20))
                        
                        tk.Button(
                            content_frame,
                            text="✓ I'll Take It Now",
                            command=reminder_window.destroy,
                            font=('Arial', 16, 'bold'),
                            bg='white',
                            fg=self.colors['accent_blue'],
                            width=20,
                            height=2,
                            relief='flat'
                        ).pack()
                        
                        break
        except Exception as e:
            print(f"Error checking medication reminders: {e}")
    
    def run(self):
        """Start the enhanced application"""
        try:
            # Set window icon and additional properties
            self.root.resizable(True, True)
            self.root.minsize(800, 600)
            
            # Focus and bring to front
            self.root.lift()
            self.root.focus_force()
            
            self.root.mainloop()
        except Exception as e:
            print(f"Application error: {e}")

# Run the enhanced application
if __name__ == "__main__":
    try:
        app = ElderLifeConnect()
        app.run()
    except Exception as e:
        print(f"Failed to start application: {e}")
        input("Press Enter to exit...")