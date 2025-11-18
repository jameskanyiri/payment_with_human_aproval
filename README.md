# PayLink + LangChain Integration

Learn how to seamlessly integrate **PayLink payments** into your **LangChain-powered AI agent** with human-in-the-loop approval workflows.

## 🎯 Overview

This tutorial demonstrates how to add real-world monetization capabilities to your AI systems by integrating PayLink payment processing with LangChain agents. You'll learn how to:

- Set up your PayLink account
- Create secure payment requests
- Invoke payment flows inside LangChain agents
- Build a smooth human-in-the-loop approval experience

Whether you're building chatbots, autonomous agents, or workflow automations, this project shows you exactly how to add payment processing to your AI systems.

## ✨ Features

- 🤖 **LangChain Agent Integration**: Seamlessly invoke PayLink payments from within your AI agent
- 👤 **Human-in-the-Loop Approval**: Review and approve payments before execution using `HumanInTheLoopMiddleware`
- 🛒 **Order Management**: Example tool for managing orders and payment status
- 🔒 **Secure Payment Processing**: Leverage PayLink's secure payment infrastructure

## 🚀 Tech Stack

- **PayLink** - [Payment infrastructure for the AI economy](https://www.paylinkai.app/)
- **LangChain** - AI agent framework
- **LangGraph** - Agent orchestration
- **Python 3.13+** - Programming language

## 📋 Prerequisites

- Python 3.13 or higher
- A PayLink account (sign up at [PayLink](https://www.paylinkai.app/))
- PayLink API credentials (API key and secret)
- OpenAI API key (for the LLM)

## 🔧 Installation

1. **Clone the repository** (if applicable):
   ```bash
   cd payment_with_human_aproval
   ```

2. **Install dependencies** using `uv` (recommended):
   ```bash
   uv sync
   ```

   Or using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   
   Create a `.env` file in the project root:
   ```env
   # PayLink Credentials
   PAYLINK_API_KEY=your_paylink_api_key
   PAYLINK_API_SECRET=your_paylink_api_secret
   
   # OpenAI Credentials
   OPENAI_API_KEY=your_openai_api_key
   ```

## 📁 Project Structure

```
payment_with_human_aproval/
├── src/
│   ├── agent.py              # Main LangChain agent with PayLink integration
│   └── tools/
│       └── get_orders.py     # Example tool for fetching orders
├── main.py                   # Entry point
├── langgraph.json           # LangGraph configuration
├── pyproject.toml           # Project dependencies
└── README.md                # This file
```

## 🎓 Key Concepts

### 1. PayLink Tools Integration

The agent uses `PayLinkTools` from the PayLink LangChain integration to access payment functionality:

```python
from paylink.intergrations.langchain_tools import PayLinkTools

paylink_client = PayLinkTools()
payment_tools = paylink_client.list_tools()
```

These tools are automatically made available to your agent, allowing it to:
- Create payment requests
- Process STK push payments
- Check payment status

### 2. Human-in-the-Loop Approval

The agent uses `HumanInTheLoopMiddleware` to pause execution and request human approval for payment operations:

```python
from langchain.agents.middleware import HumanInTheLoopMiddleware

middleware=[
    HumanInTheLoopMiddleware(
        interrupt_on={
            "stk_push": {
                "allowed_decisions": ['approve', 'reject', "edit"]
            }
        },
        description_prefix="Please review the following payment request and decide what to do:",
    )
]
```

When the agent attempts to execute a payment (like `stk_push`), it will pause and wait for human approval with options to:
- **Approve**: Execute the payment
- **Reject**: Cancel the payment
- **Edit**: Modify the payment parameters

### 3. Custom Tools

The project includes an example `get_orders` tool that demonstrates how to integrate your own business logic:

```python
@tool("get_orders", description=TOOL_DESCRIPTION)
def get_orders(
    payment_status: Literal["paid", "pending", "failed"] | None = None,
) -> list[dict]:
    """Return orders in the cart, optionally filtered by payment status."""
    # Implementation...
```

## 🚦 Usage

### Running the Agent

Start the LangGraph development server:

```bash
langgraph dev
```

This will start the agent and make it available at `http://localhost:2024`.

### Interacting with the Agent

Once the server is running, you can interact with your agent through the LangGraph Studio interface or via API calls.

**Example conversation flow:**

1. Agent: "I can help you with orders and payments. What would you like to do?"
2. User: "Show me pending orders"
3. Agent: *Uses `get_orders` tool with `payment_status="pending"`*
4. Agent: "I found 2 pending orders. Would you like me to process payment for any of them?"
5. User: "Yes, process payment for Item 2"
6. Agent: *Prepares payment request and pauses for approval*
7. System: "⚠️ Approval Required: Review the payment request for Item 2 (400 Ksh)"
8. User: *Reviews and approves*
9. Agent: *Executes payment via PayLink*

## 🔐 Security Best Practices

- **Never commit `.env` files** - Add `.env` to your `.gitignore`
- **Use environment variables** for all sensitive credentials
- **Keep API keys secure** and never expose them in client-side code

## 📚 Learn More

- [PayLink Website](https://www.paylinkai.app/) - Learn more about PayLink
- [PayLink Documentation](https://paylink-c15dc1ba.mintlify.app/) - Full API documentation and guides
- [LangChain Documentation](https://python.langchain.com)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph)

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📝 License

[Add your license here]

## 🎥 Video Tutorial

This project accompanies a video tutorial. Watch it to see the integration in action!

---

**Built with ❤️ using PayLink and LangChain**

