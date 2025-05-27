from crew import CrewGenerator

def main():
    # Run the crew executor to generate the blog post
    result = CrewGenerator().crew().kickoff()
    print(result)

    # Save the result to a markdown file
    with open("blog_output.md", "w", encoding="utf-8") as f:
        f.write(str(result))

    print("✅ Crew AI execution complete. Output saved to blog_output.md.")

if __name__ == "__main__":
    main()
