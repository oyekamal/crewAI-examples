from textwrap import dedent
from crewai import Task

class StoryTasks():
	def Writer_task(self, agent, story):
		return Task(description=dedent(f"""
                                 
            You will create a story using following instructions:
            Instructions
			------------
   
   
			Develop a compelling plot that is suitable for the target age group.
			Create relatable and engaging characters.
			Incorporate educational elements that align with learning objectives.
			Ensure the language and vocabulary are appropriate for the target audience.

			Story:
    		{story}

			Your Final answer must be the full story, only the text.
			"""),
			agent=agent
		)

	def Editor_task(self, agent, story):
		return Task(description=dedent(f"""\
                                 
            You will create a story using following instructions:
            Instructions
			------------
			Correct grammatical, punctuation, and spelling errors.
			Improve the flow and readability of the story.
			Ensure consistency in tone and style.
			Provide feedback to the author for any necessary revisions.
			
			Story:
    		{story}


			Your Final answer must be the full story, only the text.
			"""),
			agent=agent
		)

	def Illustrator_task(self, agent, story):
		return Task(description=dedent(f"""\
                                 
            You will create a story using following instructions:
            Instructions
			------------
			Create illustrations that match the story's themes and characters.
			Ensure artwork is colorful, engaging, and appropriate for the target age group.
			Collaborate with the author and editor to ensure illustrations complement the text.
			Story:
    		{story}


			Your Final answer must be the full story, only the text.
			"""),
			agent=agent
		)
  
	def Educational_Consultant_task(self, agent, story):
		return Task(description=dedent(f"""\
                                 
            You will create a story using following instructions:
            Instructions
			------------
			Review the story for educational content and developmental appropriateness.
			Suggest modifications to enhance the educational value.
			Ensure the story aligns with relevant learning standards and objectives.
						
   			Story:
    		{story}


			Your Final answer must be the full story, only the text.
			"""),
			agent=agent
		)
  
	def Psychologist_task(self, agent, story):
		return Task(description=dedent(f"""\
                                 
            You will create a story using following instructions:
            Instructions
			------------
			Assess the story for any content that could be distressing or harmful.
			Make the story more supportive of healthy development.
			Incorporate positive behavioral and emotional messages.
			
			Story:
    		{story}


			Your Final answer must be the full story, only the text.
			"""),
			agent=agent
		)
  
	def Librarian_task(self, agent, story):
		return Task(description=dedent(f"""\
                                 
            You will create a story using following instructions:
            Instructions
			------------
			Evaluate the story's appeal to children.
			Ensure the story fits within the broader context of children's literature.

			Story:
    		{story}


			Your Final answer must be the full story, only the text.
			"""),
			agent=agent
		)
  
	def Teacher_task(self, agent, story):
		return Task(description=dedent(f"""\
                                 
            You will create a story using following instructions:
            Instructions
			------------
			The story for its applicability in a classroom setting.

			Story:
    		{story}


			Your Final answer must be the full story, only the text.
			"""),
			agent=agent
		)