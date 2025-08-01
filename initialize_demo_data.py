"""
Demo Data Initialization Script for HackaAIverse 2024
This script populates the system with sample data for demonstration purposes
"""

import json
import os
from datetime import datetime, timedelta
from data_manager import DataManager
from config import Config, DEFAULT_PROBLEMS

def initialize_demo_data():
    """Initialize the system with comprehensive demo data"""
    
    print("🚀 Initializing HackaAIverse Demo Data...")
    
    # Initialize data manager
    data_manager = DataManager()
    
    # 1. Initialize Problem Statements
    print("📝 Adding problem statements...")
    
    # Clear existing problems and add default ones
    with open(Config.PROBLEM_FILE, 'w') as f:
        json.dump(DEFAULT_PROBLEMS, f, indent=2)
    
    # Add additional generated problems
    additional_problems = [
        {
            "id": "prob_005",
            "title": "Smart Campus Assistant",
            "description": "Create an AI-powered chatbot that helps students navigate campus life, from finding classrooms to getting dining hall menus and event information.",
            "category": "AI/ML",
            "difficulty": "Easy",
            "tech_stack": ["Python", "NLP", "Chatbot Framework", "API Integration"]
        },
        {
            "id": "prob_006",
            "title": "Blockchain Voting System",
            "description": "Build a secure, transparent voting system using blockchain technology for student elections and organizational decisions.",
            "category": "Web3/Blockchain",
            "difficulty": "Hard",
            "tech_stack": ["Solidity", "Web3.js", "React", "Ethereum"]
        },
        {
            "id": "prob_007",
            "title": "AR Study Companion",
            "description": "Develop an augmented reality application that helps students visualize complex concepts in subjects like chemistry, physics, or mathematics.",
            "category": "Gaming",
            "difficulty": "Medium",
            "tech_stack": ["Unity", "ARCore", "C#", "3D Modeling"]
        }
    ]
    
    problems = data_manager.get_problems()
    problems.extend(additional_problems)
    data_manager.save_json(Config.PROBLEM_FILE, problems)
    
    # 2. Register Sample Teams
    print("👥 Registering sample teams...")
    
    sample_teams = [
        {
            "team_name": "AI Innovators",
            "members": ["John Doe", "Jane Smith", "Alex Chen"],
            "email": "ai.innovators@example.com",
            "college": "IIT Delhi",
            "contact_number": "+91-9876543210"
        },
        {
            "team_name": "Code Crusaders",
            "members": ["Sarah Wilson", "Mike Johnson"],
            "email": "codecrusaders@example.com", 
            "college": "DTU",
            "contact_number": "+91-9876543211"
        },
        {
            "team_name": "Tech Titans",
            "members": ["Priya Sharma", "Rahul Kumar", "Anita Patel", "David Lee"],
            "email": "techtitans@example.com",
            "college": "NSUT",
            "contact_number": "+91-9876543212"
        },
        {
            "team_name": "Quantum Coders",
            "members": ["Lisa Zhang", "Carlos Rodriguez", "Aisha Khan"],
            "email": "quantumcoders@example.com",
            "college": "IIT Delhi", 
            "contact_number": "+91-9876543213"
        },
        {
            "team_name": "Digital Dreamers",
            "members": ["Ravi Gupta", "Sneha Reddy"],
            "email": "digitaldreamers@example.com",
            "college": "DTU",
            "contact_number": "+91-9876543214"
        }
    ]
    
    for team_data in sample_teams:
        try:
            team_id = data_manager.register_team(
                team_name=team_data["team_name"],
                members=team_data["members"],
                email=team_data["email"],
                college=team_data["college"],
                contact_number=team_data["contact_number"]
            )
            print(f"✅ Registered team: {team_data['team_name']} (ID: {team_id})")
        except ValueError as e:
            print(f"⚠️ Team {team_data['team_name']} already exists")
    
    # 3. Submit Sample Projects
    print("📤 Submitting sample projects...")
    
    sample_projects = [
        {
            "team_name": "AI Innovators",
            "project_title": "EcoTrack: Smart Carbon Footprint Analyzer",
            "description": "An AI-powered mobile application that analyzes daily activities and calculates environmental impact using computer vision and machine learning. Users can scan products, track transportation, and receive personalized sustainability recommendations.",
            "github_link": "https://github.com/ai-innovators/ecotrack",
            "demo_link": "https://ecotrack-demo.herokuapp.com",
            "tech_stack": ["Python", "TensorFlow", "React Native", "Firebase", "Computer Vision"],
            "problem_id": "prob_003"
        },
        {
            "team_name": "Code Crusaders",
            "project_title": "MindfulAI: Mental Health Companion",
            "description": "A comprehensive mental health platform that uses NLP to analyze text and voice inputs for stress detection, provides personalized coping strategies, and connects users with appropriate resources and support networks.",
            "github_link": "https://github.com/codecrusaders/mindfulai",
            "demo_link": "https://mindfulai-demo.netlify.app",
            "tech_stack": ["Python", "NLTK", "React", "Node.js", "MongoDB"],
            "problem_id": "prob_001"
        },
        {
            "team_name": "Tech Titans",
            "project_title": "GameLearn: Interactive AI Education",
            "description": "An engaging browser-based game that teaches AI and machine learning concepts through interactive puzzles, coding challenges, and visual demonstrations. Perfect for students new to AI.",
            "github_link": "https://github.com/techtitans/gamelearn",
            "demo_link": "https://gamelearn.vercel.app",
            "tech_stack": ["JavaScript", "Phaser.js", "Node.js", "Express", "PostgreSQL"],
            "problem_id": "prob_002"
        },
        {
            "team_name": "Quantum Coders",
            "project_title": "CareerCompass: AI-Powered Career Guide",
            "description": "An intelligent career recommendation system that analyzes resumes, academic performance, interests, and market trends to suggest optimal career paths and skill development plans for students.",
            "github_link": "https://github.com/quantumcoders/careercompass",
            "demo_link": "https://careercompass-ai.herokuapp.com",
            "tech_stack": ["Python", "scikit-learn", "Flask", "React", "PDF Processing"],
            "problem_id": "prob_004"
        }
    ]
    
    for project_data in sample_projects:
        try:
            submission_id = data_manager.submit_project(
                team_name=project_data["team_name"],
                project_title=project_data["project_title"],
                description=project_data["description"],
                github_link=project_data["github_link"],
                demo_link=project_data["demo_link"],
                tech_stack=project_data["tech_stack"],
                problem_id=project_data["problem_id"]
            )
            print(f"✅ Submitted project: {project_data['project_title']} (ID: {submission_id})")
        except ValueError as e:
            print(f"⚠️ Project submission failed: {e}")
    
    # 4. Add Sample Scores
    print("📊 Adding sample scores...")
    
    sample_scores = [
        {
            "team_name": "AI Innovators",
            "judge_name": "Dr. Rajesh Kumar",
            "scores": {"usefulness": 9, "creativity": 8, "teamwork": 9, "tech_stack": 8, "clarity": 9},
            "comments": "Excellent implementation with real-world impact. Great use of computer vision and user experience design."
        },
        {
            "team_name": "AI Innovators", 
            "judge_name": "Prof. Anita Sharma",
            "scores": {"usefulness": 8, "creativity": 9, "teamwork": 8, "tech_stack": 9, "clarity": 8},
            "comments": "Innovative approach to environmental tracking. Strong technical implementation and clear presentation."
        },
        {
            "team_name": "Code Crusaders",
            "judge_name": "Dr. Rajesh Kumar", 
            "scores": {"usefulness": 9, "creativity": 7, "teamwork": 8, "tech_stack": 7, "clarity": 8},
            "comments": "Addresses important mental health issues. Good NLP implementation, could benefit from more advanced ML models."
        },
        {
            "team_name": "Code Crusaders",
            "judge_name": "Prof. Anita Sharma",
            "scores": {"usefulness": 8, "creativity": 8, "teamwork": 9, "tech_stack": 8, "clarity": 9},
            "comments": "Well-executed project with clear social impact. Excellent team collaboration and presentation skills."
        },
        {
            "team_name": "Tech Titans",
            "judge_name": "Dr. Rajesh Kumar",
            "scores": {"usefulness": 7, "creativity": 9, "teamwork": 8, "tech_stack": 7, "clarity": 8},
            "comments": "Creative approach to education. Engaging game mechanics, could expand content depth."
        },
        {
            "team_name": "Quantum Coders",
            "judge_name": "Prof. Anita Sharma",
            "scores": {"usefulness": 8, "creativity": 7, "teamwork": 7, "tech_stack": 8, "clarity": 7},
            "comments": "Solid career guidance system. Good data analysis, presentation could be more polished."
        }
    ]
    
    for score_data in sample_scores:
        try:
            score_id = data_manager.submit_score(
                team_name=score_data["team_name"],
                judge_name=score_data["judge_name"],
                scores=score_data["scores"],
                comments=score_data["comments"]
            )
            print(f"✅ Added score for {score_data['team_name']} by {score_data['judge_name']} (ID: {score_id})")
        except Exception as e:
            print(f"⚠️ Score submission failed: {e}")
    
    # 5. Add Outreach Data
    print("📧 Adding outreach campaign data...")
    
    outreach_contacts = [
        {
            "college_name": "Indian Institute of Technology Delhi",
            "contact_person": "Dr. Rajesh Kumar",
            "contact_email": "rajesh.kumar@cse.iitd.ac.in",
            "contact_phone": "+91-11-2659-1286",
            "outreach_method": "Email",
            "status": "responded"
        },
        {
            "college_name": "Delhi Technological University",
            "contact_person": "Prof. Anita Sharma", 
            "contact_email": "anita.sharma@dtu.ac.in",
            "contact_phone": "+91-11-2787-2983",
            "outreach_method": "Email + LinkedIn",
            "status": "interested"
        },
        {
            "college_name": "Netaji Subhas University of Technology",
            "contact_person": "Dr. Vikram Singh",
            "contact_email": "vikram.singh@nsut.ac.in", 
            "contact_phone": "+91-11-2590-1000",
            "outreach_method": "WhatsApp",
            "status": "registered"
        }
    ]
    
    for contact_data in outreach_contacts:
        try:
            contact_id = data_manager.add_outreach_contact(
                college_name=contact_data["college_name"],
                contact_person=contact_data["contact_person"],
                contact_email=contact_data["contact_email"],
                contact_phone=contact_data["contact_phone"],
                outreach_method=contact_data["outreach_method"],
                status=contact_data["status"]
            )
            print(f"✅ Added outreach contact: {contact_data['college_name']} (ID: {contact_id})")
        except Exception as e:
            print(f"⚠️ Outreach contact failed: {e}")
    
    # 6. Display Summary Statistics
    print("\n📊 Demo Data Summary:")
    stats = data_manager.get_statistics()
    print(f"• Total Teams: {stats['total_teams']}")
    print(f"• Total Submissions: {stats['total_submissions']}")
    print(f"• Submission Rate: {stats['submission_rate']:.1f}%")
    print(f"• Colleges Participating: {stats['total_colleges']}")
    print(f"• Total Scores: {stats['total_scores']}")
    print(f"• Outreach Contacts: {stats['outreach_contacts']}")
    
    print("\n🏆 Current Leaderboard:")
    leaderboard = data_manager.get_leaderboard()
    for entry in leaderboard[:3]:  # Top 3 teams
        if entry["total_average"] > 0:
            print(f"{entry['rank']}. {entry['team_name']}: {entry['total_average']:.1f} points")
    
    print("\n✅ Demo data initialization complete!")
    print("🚀 You can now run the demo with: streamlit run project.py")

if __name__ == "__main__":
    initialize_demo_data()
