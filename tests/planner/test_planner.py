"""
Test for the planner
"""
from app.planner.planner import Planner

def test_create_plan_returns_tasks():
    planner = Planner()

    plan = planner.create_plan("Explain authentication")

    assert plan.goal == "Explain authentication"

    assert len(plan.tasks) > 0

    assert plan.tasks[0].title == "Scan project"