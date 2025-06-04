from core import BubbleCore
from layers import Layer
from feedback import Feedback

def run_star_protocol(steps=50):
    bubble1 = BubbleCore()
    bubble2 = BubbleCore()
    layer1 = Layer(mode='direction')
    layer2 = Layer(mode='binary')
    feedback = Feedback()

    print("Step\tBubble1\tBubble2\tLayer1\tLayer2\tFeedbackOK")
    for i in range(steps):
        b1 = bubble1.next_step()
        b2 = bubble2.next_step()
        l1 = layer1.next_element()
        l2 = layer2.next_element()
        feedback.update_feedback()
        fb = feedback.can_interact()
        print(f"{i+1}\t{b1}\t{b2}\t{l1}\t{l2}\t{fb}")

if __name__ == "__main__":
    run_star_protocol()
