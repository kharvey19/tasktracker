from typer.testing import CliRunner
from task_tracker.main import app

runner = CliRunner()

# --- Shared test data ---
initial_tasks = [
    {
        "id": "1",
        "description": "Test Task 1",
        "status": "todo",
        "createdAt": "2025-04-30T00:00:00",
        "updatedAt": ""
    },
    {
        "id": "2",
        "description": "Test Task 2",
        "status": "done",
        "createdAt": "2025-04-30T01:00:00",
        "updatedAt": "2025-04-30T01:10:00"
    }
]

# --- Utility: Create mock versions of load/save ---
def mock_load_tasks():
    return initial_tasks.copy()

def mock_save_tasks(tasks):
    global saved_tasks
    saved_tasks = tasks 

# --- Test: list command ---
def test_list(monkeypatch):
    monkeypatch.setattr("task_tracker.main.load_tasks", mock_load_tasks)
    result = runner.invoke(app, ["list"])
    assert result.exit_code == 0
    assert "Test Task 1" in result.output
    assert "Test Task 2" in result.output

def test_list_filtered(monkeypatch):
    monkeypatch.setattr("task_tracker.main.load_tasks", mock_load_tasks)
    result = runner.invoke(app, ["list", "--status", "done"])
    assert result.exit_code == 0
    assert "Test Task 2" in result.output
    assert "Test Task 1" not in result.output

# --- Test: add command ---
def test_add(monkeypatch):
    monkeypatch.setattr("task_tracker.main.load_tasks", mock_load_tasks)
    monkeypatch.setattr("task_tracker.main.save_tasks", mock_save_tasks)
    result = runner.invoke(app, ["add", "New Task"])
    assert result.exit_code == 0
    assert "New Task" in result.output
    assert any(task["description"] == "New Task" for task in saved_tasks)

# --- Test: update command ---
def test_update(monkeypatch):
    monkeypatch.setattr("task_tracker.main.load_tasks", mock_load_tasks)
    monkeypatch.setattr("task_tracker.main.save_tasks", mock_save_tasks)
    result = runner.invoke(app, ["update", "1", "Updated Description"])
    assert result.exit_code == 0
    assert any(task["id"] == "1" and task["description"] == "Updated Description" for task in saved_tasks)

# --- Test: delete command ---
def test_delete(monkeypatch):
    monkeypatch.setattr("task_tracker.main.load_tasks", mock_load_tasks)
    monkeypatch.setattr("task_tracker.main.save_tasks", mock_save_tasks)
    result = runner.invoke(app, ["delete", "2"])
    assert result.exit_code == 0
    assert not any(task["id"] == "2" for task in saved_tasks)

# --- Test: mark command ---
def test_mark(monkeypatch):
    monkeypatch.setattr("task_tracker.main.load_tasks", mock_load_tasks)
    monkeypatch.setattr("task_tracker.main.save_tasks", mock_save_tasks)
    result = runner.invoke(app, ["mark", "1", "in progress"])
    assert result.exit_code == 0
    assert any(task["id"] == "1" and task["status"] == "in progress" for task in saved_tasks)
