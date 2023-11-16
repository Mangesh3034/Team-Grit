from manim import *

class SelectionSortAnimation(Scene):
    def construct(self):
        print("Enter the number of terms")
        nums = int(input("Number of terms: "))
        block_size = 14/nums
        print("Enter the numbers separated by space")
        nums_list = list(map(int, input().split()))
        square_text_pairs = [
            (Square(fill_color=BLUE, fill_opacity=0.5, side_length=block_size*0.7, color=BLUE), Text(str(num), color=WHITE, font_size=6*block_size))
            for num in nums_list
        ]
        square_text_groups = [VGroup(square, text) for square, text in square_text_pairs]
        for i, (square, text) in enumerate(square_text_pairs):
            square.move_to([-7+block_size*(i+1/2), 0, 0])
            text.move_to(square)
        title = Text("Selection Sort", color=WHITE, font_size=30)
        title.move_to([0, 3, 0])
        self.play(Write(title))
        self.play(*[Create(group) for group in square_text_groups], run_time=1)
        for i, (square, text) in enumerate(square_text_pairs):
            new_position = [-7+block_size*(i+1/2), 0, 0]
            square_text_groups[i].move_to(new_position)
        self.selection_sort(nums_list, square_text_groups, block_size)
        self.play(FadeOut(title), *[FadeOut(group) for group in square_text_groups])

    def selection_sort(self, nums_list, square_text_groups, block_size):
        n = len(nums_list)
        for i in range(n):
            pass_string = Text("Pass: " + str(i), color=WHITE, font_size=28)
            pass_string.move_to([-4, 2, 0])
            self.add(pass_string)
            self.wait(0.5)
            min_idx = i
            for j in range(i+1, n):
                if nums_list[j] < nums_list[min_idx]:
                    min_idx = j
            for j in range(n):
                if j == i or j == min_idx:
                    self.play(square_text_groups[j][0].animate.set_color(RED), run_time=0.5)
                else:
                    self.play(square_text_groups[j][0].animate.set_color(BLUE), run_time=0.5)
            self.wait(0.5)
            if min_idx != i:
                nums_list[i], nums_list[min_idx] = nums_list[min_idx], nums_list[i]
                square_text_groups[i], square_text_groups[min_idx] = square_text_groups[min_idx], square_text_groups[i]
                self.play(
                    square_text_groups[i].animate.move_to(square_text_groups[min_idx].get_center()),
                    square_text_groups[min_idx].animate.move_to(square_text_groups[i].get_center()),
                    run_time=0.5
                )
            self.play(square_text_groups[i][0].animate.set_color(GREEN), run_time=0.5)
            self.wait(0.5)
            self.play(square_text_groups[i][0].animate.set_color(BLUE), run_time=0.5)
            for k, (square, text) in enumerate(square_text_groups):
                new_position = [-7+block_size*(k+1/2), 0, 0]
                square_text_groups[k].move_to(new_position)
            self.remove(pass_string)
        self.remove(pass_string)
        pass_string = Text("Array Sorted!", color=WHITE, font_size=28)
        pass_string.move_to([-4, 2, 0])
        self.add(pass_string)
        self.wait(1)
        self.remove(pass_string)

# Run the animation
SelectionSortAnimation().render()