from modules.llm_initializer import LLMInitializer
from modules.agent_task_builder import AgentTaskBuilder
from modules.crew_executor import CrewExecutor

def main():
    # Initialize the LLM
    llm = LLMInitializer().get_llm()
    print("✅ LLM initialized successfully.")

    # Build agents and tasks from YAML configuration
    builder = AgentTaskBuilder(llm)
    agents = builder.build_agents()
    tasks = builder.build_tasks()
    print("✅ Agents and tasks built successfully.")

    # Create the crew executor with the agents and tasks
    executor = CrewExecutor(list(agents.values()), tasks)
    print("✅ Crew executor created successfully.")

    # Run the crew executor to generate the blog post
    result = executor.run()
    # print(result)

    # Save the result to a markdown file
    with open("blog_output.md", "w", encoding="utf-8") as f:
        f.write(str(result))

    print("✅ Crew AI execution complete. Output saved to blog_output.md.")

if __name__ == "__main__":
    main()
