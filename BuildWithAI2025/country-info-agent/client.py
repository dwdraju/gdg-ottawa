import asyncio
from fastmcp import Client

async def main():
    client = Client("http://localhost:8080")
    async with client:
        result = await client.call_tool("get_company_details", {"company_name": "3 Round Stones, Inc."})
        print(result)

if __name__ == "__main__":
    asyncio.run(main())
