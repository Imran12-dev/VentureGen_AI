
import streamlit as st
from groq import Groq
from utils.prompt_template import MASTER_PROMPT

st.set_page_config(
    page_title="Startup Idea Generator",
    page_icon="💡",
    layout="wide"
)

st.title("💡 AI Startup Idea Generator")

st.write("""
Describe your startup interests or a problem you want to solve.
VentureGen AI will generate a complete startup business plan.
""")

st.divider()

# 1. Startup themes
st.subheader("1. Select Your Startup Theme")

themes = [
    "FinTech",
    "Artificial Intelligence",
    "HealthTech",
    "EdTech",
    "Agriculture Technology",
    "E-commerce",
    "ClimateTech",
    "FoodTech",
    "Logistics",
    "Cybersecurity"
]

selected_themes = st.multiselect(
    "Choose one or more themes",
    themes,
    placeholder="Select startup themes..."
)

# 2. Problem description
st.subheader("2. Describe the Problem")

problem = st.text_area(
    "What problem are you trying to solve?",
    placeholder="Example: Small businesses in Pakistan struggle to obtain financing...",
    height=150
)

# 3. Target market
st.subheader("3. Select Your Target Market")

target_market = st.selectbox(
    "Who will be your potential customers?",
    [
        "Students",
        "Small and Medium Enterprises (SMEs)",
        "General Public",
        "Farmers",
        "Corporate Organizations",
        "Healthcare Professionals",
        "Other"
    ]
)

# 4. Additional details
additional_details = st.text_area(
    "Additional requirements (Optional)",
    placeholder="Enter any additional information..."
)

st.divider()

# 5. Generate startup plan
if st.button(
    "🚀 Generate Startup Plan",
    type="primary",
    use_container_width=True
):

    if not selected_themes or not problem.strip():
        st.warning("Please select a theme and describe the problem.")

    else:
        try:
            # Connect to Groq
            client = Groq(
                api_key=st.secrets["GROQ_API_KEY"]
            )

            # Prepare user prompt
            user_prompt = f"""
            Startup Themes: {", ".join(selected_themes)}

            Problem Description: {problem}

            Target Market: {target_market}

            Additional Details: {additional_details}

            Generate a complete startup business plan
            based on the above information.
            """

            # Send request to Groq
            with st.spinner("AI is preparing your startup plan..."):

                response = client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=[
                        {
                            "role": "system",
                            "content": MASTER_PROMPT
                        },
                        {
                            "role": "user",
                            "content": user_prompt
                        }
                    ],
                    temperature=0.7,
                    max_tokens=6000
                )

                startup_plan = response.choices[0].message.content

            # Display AI response
            st.success("Your startup plan has been generated!")

            st.markdown("---")
            st.markdown("## 📋 Your AI-Generated Startup Plan")
            st.markdown(startup_plan)

            # Download option
            st.download_button(
                label="📥 Download Startup Plan",
                data=startup_plan,
                file_name="VentureGen_Startup_Plan.md",
                mime="text/markdown"
            )

        except Exception as e:
            st.error("Unable to generate your startup plan.")
            st.write("Error details:", str(e))

st.divider()

# Footer
st.markdown("""
<div style="text-align:center; color:gray; padding:15px;">
    Developed by Muhammad Imran<br>
    VentureGen AI | National Incubation Center
</div>
""", unsafe_allow_html=True)
