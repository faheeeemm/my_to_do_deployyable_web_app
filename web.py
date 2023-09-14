import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My To Do App!")
st.subheader("TO-DOs")

for todo in todos:
    checked= st.checkbox(todo,key = todo)
    if checked:
        todos.remove(todo)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add a new Todo here",
              on_change=add_todo, key='new_todo')