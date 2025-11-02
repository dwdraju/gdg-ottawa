import asyncio
import logging
import os
import csv
from typing import List, Dict, Any

from fastmcp import FastMCP

logger = logging.getLogger(__name__)
logging.basicConfig(format="[%(levelname)s]: %(message)s", level=logging.INFO)

mcp = FastMCP("Company Info MCP Server")

@mcp.tool
def get_company_location(company_name: str) -> str:
    """Fetch the location of the given company."""
    with open('us_companies.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[1] == company_name:
                return f"{company_name} is in {row[4]}, {row[5]}."
    return f"Could not find company {company_name}."

@mcp.tool
def get_company_details(company_name: str) -> str:
    """Fetch details of the given company."""
    with open('us_companies.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[1] == company_name:
                return f"Company: {row[1]}\nYear Founded: {row[3]}\nLocation: {row[4]}, {row[5]}\nCategory: {row[10]}\nBusiness Model: {row[12]}"
    return f"Could not find company {company_name}."

if __name__ == "__main__":
    logger.info(f"🚀 MCP server started on port {os.getenv('PORT', 8081)}")
    asyncio.run(
        mcp.run_async(
            transport="http",
            host="0.0.0.0",
            port=os.getenv("PORT", 8081),
        )
    )
