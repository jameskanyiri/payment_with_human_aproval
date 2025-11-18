
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from src.tools.get_orders import get_orders
from paylink.intergrations.langchain_tools import PayLinkTools

from langchain.agents.middleware import HumanInTheLoopMiddleware


llm = init_chat_model(model="gpt-4o-mini", temperature=0)

paylink_client = PayLinkTools()

payment_tools = paylink_client.list_tools()

agent = create_agent(
    tools=[get_orders] + payment_tools,
    model=llm,
    middleware=[
        HumanInTheLoopMiddleware(
        interrupt_on={
            "stk_push": {
                "allowed_decisions": ['approve', 'reject', "edit"]
            }
        },
        description_prefix="Please review the following payment request and decide what to do:",
    )],
)
