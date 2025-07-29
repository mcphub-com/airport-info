import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/Active-api/api/airport-info'

mcp = FastMCP('airport-info')

@mcp.tool()
def airport(iata: Annotated[Union[str, None], Field(description='IATA code of the airpor to retrieve')] = None,
            icao: Annotated[Union[str, None], Field(description='ICAO code of the airport to retrieve')] = None) -> dict: 
    '''Lookup an airport by its IATA or ICAO code'''
    url = 'https://airport-info.p.rapidapi.com/airport'
    headers = {'x-rapidapi-host': 'airport-info.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'iata': iata,
        'icao': icao,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
