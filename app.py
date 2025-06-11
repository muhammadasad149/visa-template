import streamlit as st
import json
import os

# Set page config
st.set_page_config(
    page_title="Visa Cover Letter Templates",
    page_icon="📋",
    layout="wide"
)

@st.cache_data
def load_templates():
    """Load templates from JSON file"""
    try:
        with open('templates.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("templates.json file not found. Please make sure it's in the same directory as app.py")
        return {}
    except json.JSONDecodeError:
        st.error("Error reading templates.json. Please check the file format.")
        return {}

def main():
    st.title("📋 Visa Cover Letter Templates")
    st.markdown("---")
    
    # Load templates
    templates = load_templates()
    
    if not templates:
        st.warning("No templates loaded. Please check your templates.json file.")
        return
    
    # Create dropdown for visa categories
    visa_categories = list(templates.keys())
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.subheader("Select Visa Category")
        selected_visa = st.selectbox(
            "Choose a visa type:",
            visa_categories,
            index=0 if visa_categories else None
        )
    
    if selected_visa and selected_visa in templates:
        with col2:
            st.subheader(f"Templates for {selected_visa}")
            
            # Get templates for selected visa
            visa_templates = templates[selected_visa]
            
            # Create tabs for different templates
            if len(visa_templates) >= 2:
                tab1, tab2 = st.tabs(["Template 1", "Template 2"])
                
                with tab1:
                    st.markdown("### Template 1")
                    st.text_area(
                        "Cover Letter Template 1:",
                        value=visa_templates[0],
                        height=400,
                        key="template1"
                    )
                    if st.button("Copy Template 1", key="copy1"):
                        st.success("Template 1 copied to clipboard!")
                
                with tab2:
                    st.markdown("### Template 2")
                    st.text_area(
                        "Cover Letter Template 2:",
                        value=visa_templates[1],
                        height=400,
                        key="template2"
                    )
                    if st.button("Copy Template 2", key="copy2"):
                        st.success("Template 2 copied to clipboard!")
            
            elif len(visa_templates) == 1:
                st.markdown("### Available Template")
                st.text_area(
                    "Cover Letter Template:",
                    value=visa_templates[0],
                    height=400,
                    key="single_template"
                )
                if st.button("Copy Template", key="copy_single"):
                    st.success("Template copied to clipboard!")
            
            else:
                st.warning(f"No templates available for {selected_visa}")
    
    # # Footer
    # st.markdown("---")
    # st.markdown(
    #     """
    #     <div style='text-align: center; color: gray;'>
    #         <p>💡 Tip: Customize these templates according to your specific situation and requirements.</p>
    #     </div>
    #     """, 
    #     unsafe_allow_html=True
    # )

if __name__ == "__main__":
    main()