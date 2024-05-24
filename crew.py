from tasks import TextGenTasks
from agents import TextGenAgents
from saveToPdf import savetoPDF
from langchain_groq import ChatGroq
from crewai import Crew
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.environ.get("GROQ_API_KEY")

tasks = TextGenTasks()
agents = TextGenAgents()
save_to_pdf = savetoPDF()

llm = ChatGroq(
    temperature = 0,
    model_name = "llama3-8b-8192",
    groq_api_key = api_key
)

print("Welcome to the Text Content Generator Using LLM Agents")
print("------------------------------------------------------")
topic = input("What is the topic:\n")

# Create agents
content_planner_agent = agents.contentPlanner(llm)
content_writer_agent = agents.contentWriter(llm)
content_editor_agent = agents.contentEditor(llm)

# Create Tasks
content_plan_task = tasks.contentPlan(agent=content_planner_agent, llm=llm)
content_write_task = tasks.contentWrite(agent=content_writer_agent, llm=llm)
content_edit_task = tasks.contentEdit(agent=content_editor_agent, llm=llm)

# Create Crew
crew = Crew(
    agents = [content_planner_agent, content_writer_agent,content_editor_agent],
    tasks = [content_plan_task, content_write_task, content_edit_task],
    verbose = 2
)

result = crew.kickoff(inputs={"topic" : topic})
print("\n---------------------------------------------------------------------------")
print(result)

output_filename = "output.pdf"
save_to_pdf.create_pdf_from_text(result, output_filename)

