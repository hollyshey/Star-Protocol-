from datetime import datetime

class StarRavenProjectEvaluator:
    def __init__(self, deadline_str="2025-07-01"):
        self.allowed_tech_types = ['Hydrogen', 'Grid', 'LDES', 'CarbonReduction']
        self.deadline = datetime.strptime(deadline_str, "%Y-%m-%d")

    def is_valid_technology(self, tech_type):
        return tech_type in self.allowed_tech_types

    def evaluate_project(self, project):
        results = {}

        results["project_name"] = project.get("project_name", "بدون‌نام")
        results["valid_technology"] = self.is_valid_technology(project.get("tech_type", ""))
        results["has_site_control"] = project.get("site_control", False)
        results["has_design"] = project.get("design_ready", False)
        results["has_funding"] = project.get("funding_ready", False)
        results["has_community_engagement"] = project.get("community_engaged", False)
        results["reuses_site"] = project.get("reuses_existing_site", False)

        # امتیازدهی: هر معیار درست ۱ امتیاز، بازسازی سایت ۰.۵ امتیاز
        score = 0
        for key in ["valid_technology", "has_site_control", "has_design", "has_funding", "has_community_engagement"]:
            if results[key]:
                score += 1
        if results["reuses_site"]:
            score += 0.5

        results["score"] = score
        results["is_ready"] = score >= 5.5  # آستانه آمادگی

        # بررسی زمان ارسال پروژه
        submitted_at = project.get("submitted_at")
        if submitted_at:
            try:
                submitted_time = datetime.strptime(submitted_at, "%Y-%m-%d")
                results["submitted_at"] = submitted_at
                results["submitted_before_deadline"] = submitted_time <= self.deadline
            except:
                results["submitted_before_deadline"] = False
        else:
            results["submitted_before_deadline"] = False

        # شرط جایزه: آماده + تأمین مالی + ثبت قبل از مهلت
        results["eligible_for_award"] = (
            results["is_ready"]
            and results["has_funding"]
            and results["submitted_before_deadline"]
        )

        # استراتژی اجرا
        if not results["has_funding"]:
            strategy = "🟧 Partially ready – secure funding before proceeding."
        elif results["is_ready"]:
            strategy = "🟩 Fully ready – project can proceed."
        else:
            strategy = "🟥 Not ready – further steps required."

        results["strategy"] = strategy
        return results


# 🌟 نمونه اجرا:
if __name__ == "__main__":
    evaluator = StarRavenProjectEvaluator()

    project_example = {
        "project_name": "پروژه نمونه",
        "tech_type": "Hydrogen",
        "site_control": True,
        "design_ready": True,
        "funding_ready": True,  # ← تامین مالی دارد
        "community_engaged": True,
        "reuses_existing_site": True,
        "submitted_at": "2025-06-20"  # ← قبل از deadline
    }

    result = evaluator.evaluate_project(project_example)

    # چاپ نتایج
    for k, v in result.items():
        print(f"{k}: {v}")
