from  nltk.chat.util import Chat,reflections
pairs=[
       ['my name is (.*)',['hi %1']],
       ['(hi|hello|hey|holla|hola)',['hey there','hi there','haayyy']],
       ['(.*) in (.*) is fun',['%1 in %2 is indeed fun']],
       ['(.*)(location|city) ?','Tokyo,Japan'],
       ['(.*)created you?',['randerson112358 did using NLTK']],
       ['how is the weather in (.*)',['the weather in %1 is amazing as always']],
       ['(.*)help(.*)',['I can help you']],
       ['(.*) your name ?',['my name is J.A.R.V.I.S']],
       ['i love you',['sorry! I have girlfriend']],
       ['bye',['see you soon']],

]
my_dummy_reflections= {
    'go':'gone',
    'hello' : 'hey there'
}
chat=Chat(pairs,my_dummy_reflections)
#chat._substitute('go hello')
chat.converse()
