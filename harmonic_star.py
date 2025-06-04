import numpy as np
import matplotlib.pyplot as plt

# تعریف حالت سکوت
SILENCE = -1

def combine_bits(a, b):
    """
    ترکیب دو حالت (0, 1, یا سکوت) و بازگشت یک وضعیت توصیفی.
    """
    if a == SILENCE and b == SILENCE:
        return 'هیچ'        # سکوت و سکوت = هیچ
    elif (a == 0 and b == 1) or (a == 1 and b == 0):
        return 'تعامل'      # 0 و 1 با هم تعامل دارند
    elif (a == 0 and b == SILENCE) or (a == SILENCE and b == 0):
        return 'نیمه فعال'  # یکی فعال و دیگری سکوت
    elif (a == 1 and b == SILENCE) or (a == SILENCE and b == 1):
        return 'نیمه خاموش' # یکی خاموش و دیگری سکوت
    else:
        return 'نامشخص'

def harmonic_wave(t, combo):
    """
    موج هارمونیک پایه بر اساس نوع ترکیب.
    """
    if combo == 'هیچ':
        return np.zeros_like(t)
    elif combo == 'تعامل':
        return np.sin(2 * np.pi * 5 * t)
    elif combo == 'نیمه فعال':
        return 0.5 * np.sin(2 * np.pi * 3 * t)
    elif combo == 'نیمه خاموش':
        return 0.5 * np.sin(2 * np.pi * 7 * t)
    else:
        return np.zeros_like(t)

class StarNode:
    """
    مدل یک گره ستاره‌ای با قابلیت تولید موج هارمونیک و الگوریتم قرنطینه.
    """
    def __init__(self, seed, freq=1.0):
        self.seed = seed
        self.freq = freq
        self.time = np.linspace(0, 1, 1024)
        self.internal_wave = self._generate_wave()
        self.status = 'فعال'
    
    def _generate_wave(self):
        wave = np.sin(2 * np.pi * self.freq * self.time)
        mod = np.cos(2 * np.pi * self.freq * 1.618 * self.time)
        return wave + mod
    
    def pulse(self):
        self.freq *= 1.059  # تغییر هارمونیک
        self.internal_wave = self._generate_wave()
        return self.internal_wave
    
    def evaluate(self):
        """
        الگوریتم قرنطینه (Harmonic Firewall) برای تشخیص رفتارهای نامعمول.
        """
        noise_level = np.std(self.internal_wave)
        if noise_level > 1.5:  # آستانه نمونه برای نویز زیاد
            self.status = 'قرنطینه'
        else:
            self.status = 'فعال'
        return self.status

def draw_star_pattern(points, sequence):
    """
    رسم الگوی ستاره‌ای نامتوالی با نقاط و توالی داده شده.
    points: لیست مختصات (x,y)
    sequence: توالی ایندکس نقاط (مثلاً [1,4,2,5,3])
    """
    import matplotlib.pyplot as plt
    plt.figure(figsize=(6,6))
    for i in range(len(sequence)-1):
        start = points[sequence[i]-1]
        end = points[sequence[i+1]-1]
        plt.plot([start[0], end[0]], [start[1], end[1]], 'b-', linewidth=2)
    # خط برگشت به نقطه اول یا مرکز (اختیاری)
    plt.scatter(*zip(*points), color='red')
    for i, p in enumerate(points, 1):
        plt.text(p[0], p[1], str(i), fontsize=12, ha='center', va='center', color='white',
                 bbox=dict(facecolor='black', edgecolor='none', boxstyle='circle'))
    plt.axis('equal')
    plt.title('الگوی ستاره‌ای نامتوالی')
    plt.show()

def main():
    # تعریف نقاط ستاره (مثلاً یک پنج‌ضلعی)
    angle = np.linspace(0, 2*np.pi, 6)[:-1]  # 5 نقطه
    radius = 1
    points = [(radius*np.cos(a), radius*np.sin(a)) for a in angle]
    
    # توالی نامتوالی (مثال)
    sequence = [1, 4, 2, 5, 3]
    
    # رسم الگو
    draw_star_pattern(points, sequence)
    
    # تولید حالت‌های مختلف برای اعضا
    inputs_a = [0, 0, 1, 1, SILENCE, SILENCE]
    inputs_b = [1, SILENCE, 0, SILENCE, 0, SILENCE]
    
    # ترکیب‌ها
    combinations = [combine_bits(a, b) for a, b in zip(inputs_a, inputs_b)]
    print("ترکیب‌های بیت‌ها:")
    for i, combo in enumerate(combinations):
        print(f"{inputs_a[i]} و {inputs_b[i]} -> {combo}")
    
    # تولید موج هارمونیک کلی
    t = np.linspace(0, 1, 500)
    total_wave = np.zeros_like(t)
    for combo in combinations:
        total_wave += harmonic_wave(t, combo)
    
    plt.plot(t, total_wave)
    plt.title('موج ترکیبی بر اساس ترکیب‌های سه‌حالته')
    plt.xlabel('زمان')
    plt.ylabel('دامنه')
    plt.show()
    
    # نمونه گره ستاره‌ای و ارزیابی
    star = StarNode(seed="∞")
    for i in range(5):
        star.pulse()
    status = star.evaluate()
    print(f"وضعیت نود ستاره‌ای پس از ارزیابی: {status}")

if __name__ == "__main__":
    main()
