import streamlit as st

#make title
st.title('Python Quiz')

q1 = st.radio('Question 1: Is the following statement true or false: "Python is better than MATLAB."', ["True", "False"], None)

if q1 == "True":
    st.session_state.correct1 = True
else:
    st.session_state.correct1 = False

check1 = st.button('Check answer if you really need to')

if check1:
    if st.session_state.correct1 == True:
        st.success('That one was easy!')
    else:
        st.warning('Are you serious?!? That one was supposed to be easy!!')

q2 = st.radio('Question 2: Which of the following produces "True" or "False"?', ['Integer', 'String', 'Boolean'], None)

if q2 == "Boolean":
    st.session_state.correct2 = True
else:
    st.session_state.correct2 = False

check2 = st.button('You really should NOT have to check, but if you do, click here')

if check2:
    if st.session_state.correct2 == True:
        st.success("If you got this one wrong... there's something wrong with you.")
    else:
        st.warning("There must be something wrong with you.")

q3 = st.radio('Question 3: Which will give an error?', ['my_string[1] = 1', 'my_list[1] = 1', 'my_string = 1'], None)

if q3 == 'my_string[1] = 1':
    st.session_state.correct3 = True
else:
    st.session_state.correct3 = False

check3 = st.button("I'm actually not going to let you check this one.")

if check3:
    if st.session_state.correct3 == True:
        st.success("Fine... you got it right. You happy? Here's a cookie: 🍪")
    else:
        st.warning("This is just sad. I told you I wasn't going to check it and you still got it wrong!")

code = '''my_string = I would like to get coffee.
for letter in my_string:
    if letter = " ":
        my_string[letter] = ""'''

st.write('Question 4: What will the following code result in?')
st.code(code, language = 'python')
q4_1 = st.checkbox('"Iwouldliketogetcoffee."')
q4_2 = st.checkbox('"I  would  like  to  get  coffee."')
q4_3 = st.checkbox('This will result in an error')

if q4_3 == True and q4_2 == False and q4_1 == False:
    st.session_state.correct4 = True
else:
    st.session_state.correct4 = False

check4 = st.button('Fine... check your answer.')

if check4:
    if st.session_state.correct4 == True:
        st.success("Yep, that's right.")
    else:
        st.warning("Nope, wrong. (I give up)")

q5 = st.multiselect('Question 5: Which of the items below is a "type"', ['Integer', 'String', 'Boolean', 'Thing',])

if 'Integer' in q5 and 'String' in q5 and 'Boolean' in q5:
    st.session_state.correct5 = True
else:
    st.session_state.correct5 = False

check5 = st.button('Check Answer')

if check5:
    if st.session_state.correct5 == True:
        st.success("Correct.")
    else:
        st.warning("Incorrect.")

st.divider()

terms = st.checkbox('Check this box to agree to our terms and services')

if terms:
    st.info('This box actually does nothing, but I bet you clicked it because you thought you had to.')

correct = 0

if st.session_state.correct1 == True:
    correct += 1
if st.session_state.correct2 == True:
    correct += 1
if st.session_state.correct3 == True:
    correct += 1
if st.session_state.correct4 == True:
    correct += 1
if st.session_state.correct5 == True:
    correct += 1

st.divider()

st.write('Click the button below to submit the quiz')
submit = st.button('Submit')

finished = 0

if submit:
    if correct < 5 and correct != 0:
        st.divider()
        st.info(f'You scored {correct} out of {len(st.session_state)}! I literally let you change your answers to get them correct... 😭')
        finished = st.button('Finished?')
    elif correct == 0:
        st.divider()
        st.info(f'Hell no.')
        finished = st.button('Click this button and actually try to get something right.')
    else:
        st.divider()
        st.info(f"You scored {correct} out of {len(st.session_state)}! I actually got {correct + 1} out of {len(st.session_state)}, but I guess that's pretty good.")
        st.balloons()
        finished = st.button('Finished?')

if finished:
    st.rerun()


