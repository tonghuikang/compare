Package Management
- ONLY use uv, NEVER pip
- Installation: uv add package
- Running tools: uv run tool
- Upgrading: uv add --dev package --upgrade-package package
- FORBIDDEN: uv pip install, @latest syntax

Formatting
- (note: only apply to files in the current directory)
- Format: uv run --frozen ruff format *.py
- Check: uv run --frozen ruff check *.py
- Fix: uv run --frozen ruff check *.py --fix
- Sort imports: uv run --frozen ruff check --select I *.py --fix

Serving
- `nohup python3 -m http.server 64088 > server.log 2>&1 &`

Warnings
- Put any API keys in code
