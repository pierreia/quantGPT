import streamlit as st
from createLLM import create_assistant

st.title('🤖 QuantLLM: an automated crypto strategy Generator and backtester.')

st.markdown("""QuantLLM lets you easily generate, optimise and backtest a crypto trading just from a prompt. Running with backtrader, it uses a standardized template to run any strategy. 
            Quant LLM can even generate its own original strategies.""")


st.markdown("## Add your OpenAI API key to create your quant assistant")
st.write("This step will create an openAI assistant, providing it the necessary files and instruction. The assistant id will be stored in .env.")

api_key = st.text_input("Your openAI API key")


if st.button('Create assistant'):
    assistant_id = create_assistant(api_key)
    lines = [f'OPENAI_API_KEY={api_key} \n', f"OPENAI_ASSISTANT_ID={assistant_id}"]
    if assistant_id is not None:
        with open('.env','w') as f:
            f.writelines(lines)
        st.write('Successfully Generated Assistant', assistant_id)
    else:
        st.write('Error generating agent')

