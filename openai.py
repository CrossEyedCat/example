from promptify import OpenAI, Prompter

sentence     =  """The patient is a 93-year-old female with a medical                   
                history of chronic right hip pain, osteoporosis,                    
                hypertension, depression, and chronic atrial                        
                fibrillation admitted for evaluation and management                
                of severe nausea and vomiting and urinary tract                
                infection"""

model        = OpenAI('sk-...YLvx', model = "gpt-3.5-turbo")
nlp_prompter = Prompter(model)


result       = nlp_prompter.fit('ner.jinja',
                          domain      = 'medical',
                          text_input  = sentence,
                          labels      = None)

eval(result['text'])