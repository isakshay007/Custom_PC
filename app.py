import streamlit as st
from lyzr_automata.ai_models.openai import OpenAIModel
from lyzr_automata import Agent, Task
from lyzr_automata.pipelines.linear_sync_pipeline import LinearSyncPipeline
from PIL import Image
from lyzr_automata.tasks.task_literals import InputType, OutputType
import os

# Set the OpenAI API key
os.environ["OPENAI_API_KEY"] = st.secrets["apikey"]

st.markdown(
    """
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

image = Image.open("./logo/lyzr-logo.png")
st.image(image, width=150)

# App title and introduction
st.title("Custom PC Build Guide")
st.markdown("Welcome to the Custom PC Build Guide! Tell us your budget and what you need, and we'll help you build the perfect PC, tailored just for you.")
st.markdown("            1) Determine Your Budget.")
st.markdown("            2) Mention your needs (Primary Use,Preferred Brands if any and etc).")
st.markdown("            3) Provide additional information if any like Such as RGB lighting, quiet operation, overclocking capabilities, etc.")
input = st.text_input(" Please enter the above details:",placeholder=f"""Type here""")

open_ai_text_completion_model = OpenAIModel(
    api_key=st.secrets["apikey"],
    parameters={
        "model": "gpt-4-turbo-preview",
        "temperature": 0.2,
        "max_tokens": 1500,
    },
)


def generation(input):
    generator_agent = Agent(
        role=" Expert PC BUILDER and CUSTOMIZATION CONSULTANT ",
        prompt_persona=f"Your task is to GUIDE users through the process of building their own CUSTOMIZED PC, tailored to their budget and specific needs, including primary use, preferred brands, and additional requirements such as RGB lighting, quiet operation, overclocking capabilities, etc.")
    prompt = f"""
You are an Expert PC BUILDER and CUSTOMIZATION CONSULTANT. Your task is to GUIDE users through the process of building their own CUSTOMIZED PC, tailored to their budget and specific needs, including primary use, preferred brands, and additional requirements such as RGB lighting, quiet operation, overclocking capabilities, etc.

Here's how you will EXECUTE this task:

1. ANALYZE the information provided by the user regarding their BUDGET , their  PRIMARY USE for the PC (e.g., gaming, professional work, general use) , their PREFERRED BRANDS if any they wish to incorporate into their build and any other SPECIAL REQUIREMENTS like RGB lighting, noise reduction features, or overclocking support etc.

2. ANALYZE the provided information again to determine the most SUITABLE COMPONENTS that align with the user's needs and budget.

3. RECOMMEND a list of suitable components (CPU, GPU, motherboard, RAM, storage solutions) that MATCH the user's criteria.

4. EXPLAIN why each component was chosen and how it fits into the overall BUILD PLAN briefly.

5. PROVIDE STEP-BY-STEP INSTRUCTIONS on how to ASSEMBLE these components into a functioning PC.

You MUST ensure that your instructions are CLEAR and EASY TO FOLLOW so that even users new to PC building can understand.

"""

    generator_agent_task = Task(
        name="Generation",
        model=open_ai_text_completion_model,
        agent=generator_agent,
        instructions=prompt,
        default_input=input,
        output_type=OutputType.TEXT,
        input_type=InputType.TEXT,
    ).execute()

    return generator_agent_task 
   
if st.button("Guide!"):
    solution = generation(input)
    st.markdown(solution)

with st.expander("ℹ️ - About this App"):
    st.markdown("""
    This app uses Lyzr Automata Agent . For any inquiries or issues, please contact Lyzr.

    """)
    st.link_button("Lyzr", url='https://www.lyzr.ai/', use_container_width=True)
    st.link_button("Book a Demo", url='https://www.lyzr.ai/book-demo/', use_container_width=True)
    st.link_button("Discord", url='https://discord.gg/nm7zSyEFA2', use_container_width=True)
    st.link_button("Slack",
                   url='https://join.slack.com/t/genaiforenterprise/shared_invite/zt-2a7fr38f7-_QDOY1W1WSlSiYNAEncLGw',
                   use_container_width=True)