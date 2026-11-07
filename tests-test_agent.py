from src_agent_tools import call_tool
def test_tool(): assert call_tool('calculator', expr='2+2')['result']==4
def test_unknown():
    try: call_tool('nope')
    except AssertionError: assert True
