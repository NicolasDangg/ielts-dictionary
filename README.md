# All-in-One MCP

This project is an all-in-one MCP (Multi-purpose chatbot) that provides access to a variety of tools, including a dictionary, game deals, and a free games finder.

## Features

- **Dictionary**: Get definitions of English words using the Merriam-Webster Collegiate Dictionary.
- **Game Deals**: Find the latest game deals under $10 from popular stores.
- **Free Games**: Discover free-to-play games sorted by name and platform.

## Built With

- [FastMCP](https://github.com/your-username/fastmcp) - A framework for building multi-purpose chatbots.

## Getting Started

To get started, you'll need to have Python 3 installed on your system. You'll also need to get an API key from Merriam-Webster.

### Prerequisites

- Python 3.10 or higher
- Pip

### Installation

1. Clone the repo:
   ```sh
   git clone https://github.com/your-username/all-in-one-mcp.git
   ```
2. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory and add your Merriam-Webster API key:
   ```
   MERRIAM_API="your-api-key"
   ```

### Obtaining a Merriam-Webster API Key

1. Go to the [Merriam-Webster Developer Center](https://dictionaryapi.com/register/index) and sign up for a free account.
2. Once you're logged in, you'll find your API key under the "My Keys" section.
3. Copy the key and paste it into your `.env` file.

## Usage

To start the MCP, run the following command in the root directory:

```sh
python main.py
```

This will start the FastMCP server, and you can now access the tools through the provided interface.
