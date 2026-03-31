"""Exceções customizadas para o módulo de processamento."""


class ProcessorError(Exception):
    """Exceção base para erros de processamento."""

    pass


class LLMError(ProcessorError):
    """Exceção para erros relacionados ao LLM."""

    pass


class LLMAPIError(LLMError):
    """Erro ao chamar a API do LLM."""

    def __init__(self, message: str, status_code: int | None = None):
        self.status_code = status_code
        super().__init__(message)


class LLMConfigurationError(LLMError):
    """Erro de configuração do LLM (ex: API key ausente)."""

    pass


class LLMRateLimitError(LLMError):
    """Erro de limite de taxa da API."""

    pass


class LLMTimeoutError(LLMError):
    """Timeout ao chamar a API do LLM."""

    pass


class TokenLimitExceededError(LLMError):
    """Erro quando o prompt excede o limite de tokens."""

    def __init__(self, message: str, token_count: int, max_tokens: int):
        self.token_count = token_count
        self.max_tokens = max_tokens
        super().__init__(message)
