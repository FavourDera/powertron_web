from anus.core.orchestrator import AgentOrchestrator

def get_power_bot_response(message: str) -> str:
    orchestrator = AgentOrchestrator(config_path="ANUS-main/ANUS-main/config.yaml")
    result = orchestrator.execute_task(message)
    # Try to extract a user-friendly answer
    if isinstance(result, dict):
        if 'answer' in result:
            return str(result['answer'])
        if 'result' in result:
            return str(result['result'])
    return str(result) 