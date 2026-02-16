import json
from typing import Dict, Any
import logging

class DashboardConnector:
    def __init__(self) -> None:
        self.config = config
        self.logger = logging.getLogger(self.__class__.__name__)

    async def send_strategy_to_dashboard(self, strategy: Dict[str, Any]) -> bool:
        try:
            # Example API call
            response = await self._make_request("POST", "https://dashboard.example.com/strategies", json=strategy)
            if response.status == 200:
                return True
            else:
                self.logger.error(f"Failed to send strategy. Status: {response.status}")
                return False
        except Exception as e:
            self.logger.error(f"Error sending strategy: {str(e)}")
            return False

    async def _make_request(self, method: str, url: str, data: Optional[Dict[str, Any]] = None) -> aiohttp.ClientResponse:
        session = aiohttp.ClientSession()
        try:
            async with session.request(method, url, json=data) as response:
                return response
        except Exception as e:
            self.logger.error(f"Request failed: {str(e)}")
            raise
```

### Explanation
The solution is designed to be modular and scalable. Each component handles specific tasks, ensuring clarity and maintainability. The use of asynchronous data collection improves efficiency, while error handling and logging provide robustness. Configuration management allows for easy adjustments, and the dashboard integration ensures human oversight.

This approach ensures that the system can evolve with the ecosystem's needs, providing a solid foundation for future enhancements and scalability.