import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import json
import os

class ElderLifeConnect:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ElderLife Connect")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f8ff')
        
        # Data storage
        self.user_data = self.load_user_data()
        self.medications = self.user_data.get('medications', [])
        self.health_records = self.user_data.get('health_records', [])
        self.appointments = self.user_data.get('appointments', [])
        
        # Configure styles for elder-friendly interface
        self.setup_styles()
        
        # Initialize main interface
        self.create_main_interface()
        
    def setup_styles(self):
        """Configure styles for better accessibility"""
        try:
            style = ttk.Style()
            style.configure('Large.TButton', font=('Arial', 14, 'bold'), padding=10)
            style.configure('Header.TLabel', font=('Arial', 18, 'bold'), background='#f0f8ff')
            style.configure('Info.TLabel', font=('Arial', 12), background='#f0f8ff')
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
        
        # Default data
        return {
            'medications': [
                {
                    'name': 'Blood Pressure Medicine',
                    'dosage': '10mg',
                    'schedule': ['08:00', '20:00'],
                    'taken_today': {'08:00': False, '20:00': False}
                },
                {
                    'name': 'Vitamin D',
                    'dosage': '1000 IU',
                    'schedule': ['09:00'],
                    'taken_today': {'09:00': False}
                }
            ],
            'health_records': [],
            'appointments': [
                {
                    'date': '2025-06-05',
                    'time': '10:00',
                    'doctor': 'Dr. Smith',
                    'type': 'Regular Checkup'
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
    
    def create_main_interface(self):
        """Create the main dashboard interface"""
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()
            
        # Main title
        title_label = ttk.Label(self.root, text="ElderLife Connect", style='Header.TLabel')
        title_label.pack(pady=20)
        
        # Current time
        time_label = ttk.Label(self.root, text=f"Today: {datetime.now().strftime('%A, %B %d, %Y')}", 
                              style='Info.TLabel')
        time_label.pack(pady=5)
        
        # Main menu buttons
        button_frame = tk.Frame(self.root, bg='#f0f8ff')
        button_frame.pack(pady=30)
        
        # Large, accessible buttons
        buttons = [
            ("💊 My Medications", self.show_medications),
            ("📊 Health Tracking", self.show_health_tracking),
            ("👨‍⚕️ Appointments", self.show_appointments),
            ("🆘 Emergency Help", self.emergency_help),
            ("⚙️ Settings", self.show_settings)
        ]
        
        for i, (text, command) in enumerate(buttons):
            btn = tk.Button(button_frame, text=text, command=command,
                          font=('Arial', 16, 'bold'), width=20, height=2,
                          bg='#4a90e2', fg='white', relief='raised', bd=3)
            btn.pack(pady=10)
            
        # Check for medication reminders
        self.check_medication_reminders()
    
    def show_medications(self):
        """Display medication management interface"""
        try:
            # Clear window
            for widget in self.root.winfo_children():
                widget.destroy()
                
            # Header
            header_frame = tk.Frame(self.root, bg='#f0f8ff')
            header_frame.pack(fill='x', padx=20, pady=10)
            
            ttk.Label(header_frame, text="💊 My Medications", style='Header.TLabel').pack(side='left')
            
            back_btn = tk.Button(header_frame, text="🏠 Home", command=self.create_main_interface,
                               font=('Arial', 12), bg='#808080', fg='white')
            back_btn.pack(side='right')
            
            # Medication list
            med_frame = tk.Frame(self.root, bg='#f0f8ff')
            med_frame.pack(fill='both', expand=True, padx=20, pady=10)
            
            if not self.medications:
                no_med_label = tk.Label(med_frame, text="No medications configured", 
                                      font=('Arial', 14), bg='#f0f8ff')
                no_med_label.pack(pady=50)
                return
            
            for i, med in enumerate(self.medications):
                # Create medication card
                card = tk.Frame(med_frame, bg='white', relief='raised', bd=2)
                card.pack(fill='x', pady=10, padx=10)
                
                # Medication info
                info_frame = tk.Frame(card, bg='white')
                info_frame.pack(fill='x', padx=15, pady=10)
                
                name_label = tk.Label(info_frame, text=med['name'], font=('Arial', 14, 'bold'), bg='white')
                name_label.pack(anchor='w')
                
                dosage_label = tk.Label(info_frame, text=f"Dosage: {med['dosage']}", 
                                      font=('Arial', 12), bg='white')
                dosage_label.pack(anchor='w')
                
                # Schedule and status
                for time_slot in med['schedule']:
                    schedule_frame = tk.Frame(card, bg='white')
                    schedule_frame.pack(fill='x', padx=15, pady=5)
                    
                    time_label = tk.Label(schedule_frame, text=f"Time: {time_slot}", 
                                        font=('Arial', 12), bg='white')
                    time_label.pack(side='left')
                    
                    taken = med['taken_today'].get(time_slot, False)
                    status = "✅ Taken" if taken else "❌ Not Taken"
                    status_color = "green" if taken else "red"
                    
                    status_label = tk.Label(schedule_frame, text=status, 
                                          font=('Arial', 12, 'bold'), 
                                          fg=status_color, bg='white')
                    status_label.pack(side='left', padx=20)
                    
                    if not taken:
                        take_btn = tk.Button(schedule_frame, text="Take Now", 
                                           command=lambda m=i, t=time_slot: self.mark_medication_taken(m, t),
                                           font=('Arial', 10), bg='#4a90e2', fg='white')
                        take_btn.pack(side='right')
                        
        except Exception as e:
            messagebox.showerror("Error", f"Error displaying medications: {str(e)}")
            self.create_main_interface()
    
    def mark_medication_taken(self, med_index, time_slot):
        """Mark medication as taken"""
        try:
            if med_index < len(self.medications):
                self.medications[med_index]['taken_today'][time_slot] = True
                self.save_user_data()
                messagebox.showinfo("Medication Taken", 
                              f"✅ {self.medications[med_index]['name']} marked as taken!")
                self.show_medications()  # Refresh the view
        except Exception as e:
            messagebox.showerror("Error", f"Error marking medication: {str(e)}")
    
    def show_health_tracking(self):
        """Display health tracking interface"""
        try:
            # Clear window
            for widget in self.root.winfo_children():
                widget.destroy()
                
            # Header
            header_frame = tk.Frame(self.root, bg='#f0f8ff')
            header_frame.pack(fill='x', padx=20, pady=10)
            
            ttk.Label(header_frame, text="📊 Health Tracking", style='Header.TLabel').pack(side='left')
            
            back_btn = tk.Button(header_frame, text="🏠 Home", command=self.create_main_interface,
                               font=('Arial', 12), bg='#808080', fg='white')
            back_btn.pack(side='right')
            
            # Health metrics input
            input_frame = tk.Frame(self.root, bg='white', relief='raised', bd=2)
            input_frame.pack(fill='x', padx=20, pady=10)
            
            ttk.Label(input_frame, text="Record Your Health Metrics", 
                     font=('Arial', 14, 'bold')).pack(pady=10)
            
            # Blood pressure
            bp_frame = tk.Frame(input_frame, bg='white')
            bp_frame.pack(pady=5)
            tk.Label(bp_frame, text="Blood Pressure:", font=('Arial', 12), bg='white').pack(side='left')
            self.bp_systolic = tk.Entry(bp_frame, font=('Arial', 12), width=5)
            self.bp_systolic.pack(side='left', padx=5)
            tk.Label(bp_frame, text="/", font=('Arial', 12), bg='white').pack(side='left')
            self.bp_diastolic = tk.Entry(bp_frame, font=('Arial', 12), width=5)
            self.bp_diastolic.pack(side='left', padx=5)
            
            # Heart rate
            hr_frame = tk.Frame(input_frame, bg='white')
            hr_frame.pack(pady=5)
            tk.Label(hr_frame, text="Heart Rate (bpm):", font=('Arial', 12), bg='white').pack(side='left')
            self.heart_rate = tk.Entry(hr_frame, font=('Arial', 12), width=10)
            self.heart_rate.pack(side='left', padx=5)
            
            # Weight
            weight_frame = tk.Frame(input_frame, bg='white')
            weight_frame.pack(pady=5)
            tk.Label(weight_frame, text="Weight (lbs):", font=('Arial', 12), bg='white').pack(side='left')
            self.weight = tk.Entry(weight_frame, font=('Arial', 12), width=10)
            self.weight.pack(side='left', padx=5)
            
            # Save button
            save_btn = tk.Button(input_frame, text="💾 Save Health Data", 
                               command=self.save_health_data,
                               font=('Arial', 12, 'bold'), bg='#4a90e2', fg='white')
            save_btn.pack(pady=15)
            
            # Recent records
            records_frame = tk.Frame(self.root, bg='white', relief='raised', bd=2)
            records_frame.pack(fill='both', expand=True, padx=20, pady=10)
            
            ttk.Label(records_frame, text="Recent Health Records", 
                     font=('Arial', 14, 'bold')).pack(pady=10)
            
            # Display recent records
            if self.health_records:
                for record in self.health_records[-5:]:  # Show last 5 records
                    record_text = f"{record['date']}: BP {record.get('bp_systolic', 'N/A')}/{record.get('bp_diastolic', 'N/A')}, HR {record.get('heart_rate', 'N/A')}, Weight {record.get('weight', 'N/A')} lbs"
                    tk.Label(records_frame, text=record_text, font=('Arial', 10), bg='white').pack(anchor='w', padx=10)
            else:
                tk.Label(records_frame, text="No health records yet", font=('Arial', 12), bg='white').pack(pady=20)
                
        except Exception as e:
            messagebox.showerror("Error", f"Error displaying health tracking: {str(e)}")
            self.create_main_interface()
    
    def save_health_data(self):
        """Save health tracking data"""
        try:
            record = {
                'date': datetime.now().strftime('%Y-%m-%d %H:%M'),
                'bp_systolic': self.bp_systolic.get() if self.bp_systolic.get() else None,
                'bp_diastolic': self.bp_diastolic.get() if self.bp_diastolic.get() else None,
                'heart_rate': self.heart_rate.get() if self.heart_rate.get() else None,
                'weight': self.weight.get() if self.weight.get() else None
            }
            
            # Only save if at least one field has data
            if any(record[key] for key in ['bp_systolic', 'bp_diastolic', 'heart_rate', 'weight']):
                self.health_records.append(record)
                self.save_user_data()
                messagebox.showinfo("Data Saved", "✅ Health data recorded successfully!")
                self.show_health_tracking()  # Refresh
            else:
                messagebox.showwarning("No Data", "Please enter at least one health metric.")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save data: {str(e)}")
    
    def show_appointments(self):
        """Display appointments interface"""
        try:
            # Clear window
            for widget in self.root.winfo_children():
                widget.destroy()
                
            # Header
            header_frame = tk.Frame(self.root, bg='#f0f8ff')
            header_frame.pack(fill='x', padx=20, pady=10)
            
            ttk.Label(header_frame, text="👨‍⚕️ My Appointments", style='Header.TLabel').pack(side='left')
            
            back_btn = tk.Button(header_frame, text="🏠 Home", command=self.create_main_interface,
                               font=('Arial', 12), bg='#808080', fg='white')
            back_btn.pack(side='right')
            
            # Appointments list
            apt_frame = tk.Frame(self.root, bg='#f0f8ff')
            apt_frame.pack(fill='both', expand=True, padx=20, pady=10)
            
            if not self.appointments:
                tk.Label(apt_frame, text="No upcoming appointments", 
                        font=('Arial', 14), bg='#f0f8ff').pack(pady=50)
            else:
                for apt in self.appointments:
                    # Appointment card
                    card = tk.Frame(apt_frame, bg='white', relief='raised', bd=2)
                    card.pack(fill='x', pady=10, padx=10)
                    
                    info_frame = tk.Frame(card, bg='white')
                    info_frame.pack(fill='x', padx=15, pady=15)
                    
                    date_label = tk.Label(info_frame, text=f"📅 {apt['date']} at {apt['time']}", 
                                        font=('Arial', 14, 'bold'), bg='white')
                    date_label.pack(anchor='w')
                    
                    doctor_label = tk.Label(info_frame, text=f"👨‍⚕️ {apt['doctor']}", 
                                          font=('Arial', 12), bg='white')
                    doctor_label.pack(anchor='w')
                    
                    type_label = tk.Label(info_frame, text=f"📋 {apt['type']}", 
                                        font=('Arial', 12), bg='white')
                    type_label.pack(anchor='w')
            
            # Telehealth button
            telehealth_btn = tk.Button(apt_frame, text="💻 Start Telehealth Session", 
                                     command=self.start_telehealth,
                                     font=('Arial', 14, 'bold'), bg='#28a745', fg='white',
                                     width=25, height=2)
            telehealth_btn.pack(pady=20)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error displaying appointments: {str(e)}")
            self.create_main_interface()
    
    def start_telehealth(self):
        """Simulate telehealth session start"""
        messagebox.showinfo("Telehealth", 
                          "📞 Connecting to your healthcare provider...\n\n" +
                          "This would normally:\n" +
                          "• Connect video call\n" +
                          "• Share your health data\n" +
                          "• Record consultation notes")
    
    def emergency_help(self):
        """Emergency help interface"""
        try:
            response = messagebox.askquestion("Emergency Help", 
                                            "🆘 Do you need immediate medical assistance?\n\n" +
                                            "Click YES to call emergency services\n" +
                                            "Click NO for non-emergency help")
            
            if response == 'yes':
                messagebox.showwarning("Emergency Services", 
                                     "📞 Calling 911...\n\n" +
                                     "Your location and medical information\n" +
                                     "have been shared with emergency services.")
            else:
                messagebox.showinfo("Non-Emergency Help", 
                                  "📞 Here are your emergency contacts:\n\n" +
                                  "• Dr. Smith: (555) 123-4567\n" +
                                  "• Family: (555) 987-6543\n" +
                                  "• Pharmacy: (555) 246-8135")
        except Exception as e:
            messagebox.showerror("Error", f"Error in emergency help: {str(e)}")
    
    def show_settings(self):
        """Display settings interface"""
        try:
            # Clear window
            for widget in self.root.winfo_children():
                widget.destroy()
                
            # Header
            header_frame = tk.Frame(self.root, bg='#f0f8ff')
            header_frame.pack(fill='x', padx=20, pady=10)
            
            ttk.Label(header_frame, text="⚙️ Settings", style='Header.TLabel').pack(side='left')
            
            back_btn = tk.Button(header_frame, text="🏠 Home", command=self.create_main_interface,
                               font=('Arial', 12), bg='#808080', fg='white')
            back_btn.pack(side='right')
            
            # Settings options
            settings_frame = tk.Frame(self.root, bg='#f0f8ff')
            settings_frame.pack(fill='both', expand=True, padx=20, pady=20)
            
            settings_options = [
                "🔔 Notification Settings",
                "👤 Profile Information", 
                "🏥 Healthcare Providers",
                "👨‍👩‍👧‍👦 Emergency Contacts",
                "🎨 Display Settings",
                "🔒 Privacy & Security"
            ]
            
            for option in settings_options:
                btn = tk.Button(settings_frame, text=option, 
                              command=lambda opt=option: self.show_setting_detail(opt),
                              font=('Arial', 14), width=30, height=2,
                              bg='white', relief='raised', bd=2)
                btn.pack(pady=10)
                
        except Exception as e:
            messagebox.showerror("Error", f"Error displaying settings: {str(e)}")
            self.create_main_interface()
    
    def show_setting_detail(self, setting_name):
        """Show setting detail (placeholder)"""
        messagebox.showinfo("Settings", f"This would open {setting_name} configuration.\n\nFeature coming soon!")
    
    def check_medication_reminders(self):
        """Check for medication reminders"""
        try:
            current_time = datetime.now().strftime('%H:%M')
            
            for med in self.medications:
                for time_slot in med['schedule']:
                    if (time_slot == current_time and 
                        not med['taken_today'].get(time_slot, False)):
                        
                        messagebox.showwarning("Medication Reminder", 
                                             f"⏰ Time to take your medication!\n\n" +
                                             f"💊 {med['name']}\n" +
                                             f"💉 {med['dosage']}")
                        break
        except Exception as e:
            print(f"Error checking medication reminders: {e}")
    
    def run(self):
        """Start the application"""
        try:
            self.root.mainloop()
        except Exception as e:
            print(f"Application error: {e}")

# Run the application
if __name__ == "__main__":
    try:
        app = ElderLifeConnect()
        app.run()
    except Exception as e:
        print(f"Failed to start application: {e}")
        input("Press Enter to exit...")