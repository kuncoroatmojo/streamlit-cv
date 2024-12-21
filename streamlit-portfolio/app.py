import streamlit as st
from PIL import Image
import os

# Konfigurasi halaman dan styling
st.set_page_config(
    page_title="Kuncoro Atmojo | CV",
    page_icon="👨‍💻",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    /* Custom fonts */
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap');
    
    /* Main styling */
    .main {
        background-color: rgb(17, 19, 20);
        color: rgb(215, 243, 245);
        font-family: 'Space Grotesk', sans-serif;
        overflow-x: hidden !important;
    }
    
    /* Headers */
    h1 {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 5rem;
        font-weight: 700;
        letter-spacing: -0.02em;
        margin-bottom: 1rem;
        color: rgb(215, 243, 245);
        line-height: 1.2;
    }
    
    .subheader {
        font-size: 1.75rem;
        color: rgba(215, 243, 245, 0.8);
        font-weight: 300;
        margin-bottom: 3rem;
    }
    
    /* Sections */
    .section {
        padding: 3rem;
        background-color: rgba(215, 243, 245, 0.03);
        border-radius: 1.5rem;
        margin-bottom: 2.5rem;
        transition: all 0.3s ease;
    }
    
    .section:hover {
        background-color: rgba(215, 243, 245, 0.05);
        transform: translateY(-5px);
    }
    
    /* Skills badges */
    .badge {
        background-color: rgba(215, 243, 245, 0.1);
        color: rgb(215, 243, 245);
        padding: 0.75rem 1.5rem;
        border-radius: 100vw;
        margin: 0.5rem;
        display: inline-block;
        transition: all 0.3s ease;
    }
    
    .badge:hover {
        background-color: rgba(215, 243, 245, 0.2);
        transform: translateY(-2px);
    }
    
    /* Timeline items */
    .timeline-item {
        border-left: 2px solid rgba(215, 243, 245, 0.2);
        padding-left: 2rem;
        margin-bottom: 2rem;
        position: relative;
    }
    
    .timeline-item:before {
        content: '';
        position: absolute;
        left: -6px;
        top: 0;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background-color: rgb(215, 243, 245);
    }
    
    /* Profile image */
    .profile-image-container img {
        border-radius: 1.5rem;
        border: none;
        filter: grayscale(20%);
        transition: all 0.3s ease;
    }
    
    .profile-image-container img:hover {
        filter: grayscale(0%);
        transform: scale(1.02);
    }
    
    /* Smooth scrolling */
    html {
        scroll-behavior: smooth;
    }
    
    /* Hide scrollbar but keep functionality */
    ::-webkit-scrollbar {
        display: none;
    }
    
    /* Social Links */
    .social-link {
        display: inline-flex;
        align-items: center;
        padding: 0.5rem 1rem;
        background-color: rgba(215, 243, 245, 0.1);
        color: rgb(215, 243, 245);
        text-decoration: none;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
        transition: all 0.3s ease;
    }
    
    .social-link:hover {
        background-color: rgba(215, 243, 245, 0.2);
        transform: translateY(-2px);
    }
    
    /* Certification Items */
    .certification-item {
        padding: 1rem;
        margin: 1rem 0;
        background-color: rgba(215, 243, 245, 0.05);
        border-radius: 0.5rem;
        transition: all 0.3s ease;
    }
    
    .certification-item:hover {
        background-color: rgba(215, 243, 245, 0.08);
        transform: translateY(-2px);
    }
    
    .certification-item .issuer {
        color: rgba(215, 243, 245, 0.7);
        font-size: 0.9rem;
    }
    
    .certification-item .date {
        color: rgba(215, 243, 245, 0.5);
        font-size: 0.8rem;
    }
    
    /* Organization headers with logos */
    .org-header {
        display: flex;
        align-items: center;
        gap: 1rem;
        margin-bottom: 1rem;
    }
    
    .org-logo {
        width: 40px;
        height: 40px;
        border-radius: 8px;
        object-fit: cover;
        background-color: white;
        padding: 2px;
    }
    
    .experience-details {
        margin: 0.5rem 0 0 0;
        padding-left: 1.5rem;
    }
    
    .experience-details li {
        margin-bottom: 0.5rem;
        color: rgba(215, 243, 245, 0.8);
    }
    
    /* Timeline adjustments for logos */
    .timeline-item {
        padding-left: 1.5rem;
    }
    
    .timeline-item:before {
        top: 1.25rem;
    }
</style>
""", unsafe_allow_html=True)

# Fungsi untuk memuat foto
def load_image(image_file):
    try:
        return Image.open(image_file)
    except:
        return None

def main():
    # Header Section with Animation
    st.markdown("<h1>Kuncoro Atmojo</h1>", unsafe_allow_html=True)
    st.markdown("<div class='subheader'>Chief Technology Officer & Cloud Architecture Specialist</div>", unsafe_allow_html=True)
    
    # Two Column Layout
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Profile Section
        image = load_image("assets/profile_photo.jpg")
        if image:
            st.markdown("<div class='profile-image-container'>", unsafe_allow_html=True)
            st.image(image, width=300)
            st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("### Contact")
        st.markdown("📍 Jakarta, Indonesia")
        st.markdown("📧 kuncoro.atmojo@gmail.com")
        
        # Add LinkedIn profile with custom styling
        st.markdown("""
            <a href="https://www.linkedin.com/in/kuncoro-atmojo-ba940a41/" 
               target="_blank" 
               class="social-link">
                <i class="fab fa-linkedin"></i> LinkedIn Profile
            </a>
        """, unsafe_allow_html=True)
        
        # Skills Section
        st.markdown("### Technical Expertise")
        skills = {
            "Cloud & DevOps": ["Cloud Architecture", "DevOps", "Google Cloud"],
            "Leadership": ["Technical Leadership", "Strategic Thinking", "Team Mentoring"],
        }
        
        for category, skill_list in skills.items():
            st.markdown(f"**{category}**")
            for skill in skill_list:
                st.markdown(f"<span class='badge'>{skill}</span>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        # Experience Section
        st.markdown("### Professional Journey")
        
        # Load logos
        fithappy_logo = load_image("assets/fithappy_logo.jpeg")
        itb_logo = load_image("assets/itb_logo.jpeg")
        iar_logo = load_image("assets/international_animal_rescue_goa_logo.jpeg")
        kijp_logo = load_image("assets/kijp_logo.jpeg")
        
        # Create columns for logo and content
        logo_col, content_col = st.columns([1, 5])
        with logo_col:
            if fithappy_logo:
                st.image(fithappy_logo, width=40)
        with content_col:
            st.markdown("""
                <div class='timeline-item'>
                    <div>
                        <strong>Chief Technology Officer</strong> | FitHappy
                    </div>
                    <ul class='experience-details'>
                        <li>Leading technical decisions and mentoring team members</li>
                        <li>Responsible for company's technology architecture and strategy</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)
        
        # Education Section
        st.markdown("### Education")
        logo_col, content_col = st.columns([1, 5])
        with logo_col:
            if itb_logo:
                st.image(itb_logo, width=40)
        with content_col:
            st.markdown("""
                <div class='timeline-item'>
                    <div>
                        <strong>Institut Teknologi Bandung (ITB)</strong>
                        <br/>2007 - 2013
                    </div>
                </div>
            """, unsafe_allow_html=True)
        
        # Volunteer Section
        st.markdown("### Organization & Volunteering")
        
        # IAR Section
        logo_col, content_col = st.columns([1, 5])
        with logo_col:
            if iar_logo:
                st.image(iar_logo, width=40)
        with content_col:
            st.markdown("""
                <div class='timeline-item'>
                    <div>
                        <strong>Field Volunteer - International Animal Rescue</strong>
                        <br/>Mar 2017 - Apr 2017
                    </div>
                    <ul class='experience-details'>
                        <li>Installed and monitored 20+ camera traps in Batutegi Forest, Lampung</li>
                        <li>Conducted biodiversity surveys and wildlife activity documentation</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)
        
        # KIJP Section
        logo_col, content_col = st.columns([1, 5])
        with logo_col:
            if kijp_logo:
                st.image(kijp_logo, width=40)
        with content_col:
            st.markdown("""
                <div class='timeline-item'>
                    <div>
                        <strong>Teacher - Komunitas Inspirasi Jelajah Pulau</strong>
                        <br/>Oktober 2017
                    </div>
                    <ul class='experience-details'>
                        <li>Taught IT industry insights to elementary students in Kemujan Island</li>
                        <li>Inspired students to dream big and pursue their goals</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)

                # Add certifications section based on LinkedIn
        st.markdown("### Certifications")
        certifications = [
            {
                "name": "Design Thinking: Implementing the Process",
                "issuer": "Project Management Institute",
                "date": "Jan 2023"
            },
            {
                "name": "Strategic Thinking",
                "issuer": "Project Management Institute",
                "date": "Jan 2023"
            },
            {
                "name": "Google Cloud Architecture",
                "issuer": "Google",
                "date": "Dec 2019"
            }
        ]
        
        for cert in certifications:
            st.markdown(f"""
                <div class='certification-item'>
                    <strong>{cert['name']}</strong><br>
                    <span class='issuer'>{cert['issuer']}</span><br>
                    <span class='date'>{cert['date']}</span>
                </div>
            """, unsafe_allow_html=True)
if __name__ == "__main__":
    main() 