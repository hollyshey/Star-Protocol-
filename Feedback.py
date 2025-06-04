class Feedback:
    def __init__(self):
        # تضمین عدم درک متقابل بین دو حباب
        self.bubble1_understands_bubble2 = False
        self.bubble2_understands_bubble1 = False

    def update_feedback(self):
        # وضعیت فیدبک را حفظ می‌کنیم تا هیچ درکی شکل نگیرد
        self.bubble1_understands_bubble2 = False
        self.bubble2_understands_bubble1 = False

    def can_interact(self):
        return not (self.bubble1_understands_bubble2 or self.bubble2_understands_bubble1)
