import typer
from .codex_client import call_codex
from .diff_utils import get_git_diff

app = typer.Typer()

@app.command()
def run(
    prompt: str,
    path: str = typer.Option(".", help="目標專案路徑"),
    dry_run: bool = typer.Option(False, help="顯示差異但不套用"),
    approve: bool = typer.Option(False, help="自動套用變更")
):
    typer.secho(f"🚀 Codex 任務: {prompt}", fg=typer.colors.GREEN)
    result = call_codex(prompt, path)

    if result["status"] != "success":
        typer.secho("❌ Codex 錯誤：", fg=typer.colors.RED)
        typer.echo(result["message"])
        raise typer.Exit()

    typer.secho("✅ STDOUT:", fg=typer.colors.BLUE)
    typer.echo(result["stdout"])

    if result["stderr"]:
        typer.secho("⚠️ STDERR:", fg=typer.colors.YELLOW)
        typer.echo(result["stderr"])

    if dry_run:
        typer.secho("📄 Git Diff:", fg=typer.colors.CYAN)
        diff = get_git_diff(path)
        typer.echo(diff)

    if approve:
        typer.secho("✅ 自動套用中...", fg=typer.colors.GREEN)
