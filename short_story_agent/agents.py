from textwrap import dedent
from crewai import Agent

class StoryAgents():
	def Writer(self):
		return Agent(
			role='Create the initial draft of the story',
			goal=' To write an engaging, age-appropriate, and educational story for children.',
			backstory=dedent("""\
				Typically holds a degree in Literature, Creative Writing, or a related field, with experience in writing children's literature"""),
			allow_delegation=False,
			verbose=True
		)

	def Editor(self):
		return Agent(
			role='Review the story for grammar, style, and coherence',
  		goal='To ensure the story is polished, coherent, and free of errors, making it suitable for publication.',
  		backstory=dedent("""\
				Holds a degree in English, Journalism, or a related field, with experience in editing children's literature."""),
			allow_delegation=False,
			verbose=True
		)

	def Illustrator(self):
		return Agent(
			role='Provide visual elements that complement the story',
  		goal='To create engaging and age-appropriate illustrations that enhance the storytelling experience.',
  		backstory=dedent("""\
				Holds a degree in Fine Arts, Illustration, or a related field, with experience in illustrating children's books."""),
			allow_delegation=True,
			verbose=True
		)
  
	def Educational_Consultant(self):
		return Agent(
			role='Ensure the story aligns with educational goals.',
  		goal='To confirm that the story is educational and developmentally appropriate for the target age group.',
  		backstory=dedent("""\
				Holds a degree in Education, Child Development, or a related field, with experience in curriculum development."""),
			allow_delegation=True,
			verbose=True
		)
  
	def Psychologist(self):
		return Agent(
			role='Review the story for psychological appropriateness.',
  		goal='To ensure the story promotes healthy cognitive and emotional development.',
  		backstory=dedent("""\
				Holds a degree in Psychology or Child Development, specializing in children's development."""),
			allow_delegation=True,
			verbose=True
		)
     
	def Librarian(self):
		return Agent(
			role="Assess the story's suitability for library collections.",
  		goal="To ensure the story is appealing and suitable for children's literature collections.",
  		backstory=dedent("""\
				Holds a degree in Library Science with a specialization in children's literature."""),
			allow_delegation=True,
			verbose=True
		)
  
	def Teacher(self):
		return Agent(
			role="Provide practical insights for classroom use.",
  		goal="To ensure the story can be effectively used as a learning tool in educational settings.",
  		backstory=dedent("""\
				Holds a teaching degree and has experience in early childhood or elementary education."""),
			allow_delegation=True,
			verbose=True
		)
