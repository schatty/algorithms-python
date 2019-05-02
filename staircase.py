"""
The staircase has n steps each under the value [-1e4..1e4]. Find maximum sum that
we can obtain by going through staricase either each step or skipping the one.
"""

def calc_max_staircase(vals):
    sum = 0

    step_cur_skip_prev = vals[0]    # Choose to step on current one and the previous is skipped
    step_cur_step_prev = vals[0]    # Choose to step on current one and the previous is stepped also
    skip_cur_step_prev = 0          # Choose to skip current one based on stepping on previous

    for v in vals[1:]:
        step_cur_skip_prev_tmp = v + skip_cur_step_prev
        step_cur_step_prev_tmp = v + max(step_cur_skip_prev, step_cur_step_prev)
        skip_cur_step_prev = max(step_cur_skip_prev, step_cur_step_prev)

        # Update accumulator
        step_cur_skip_prev = step_cur_skip_prev_tmp
        step_cur_step_prev = step_cur_step_prev_tmp

    return max(step_cur_skip_prev, step_cur_step_prev)

if __name__ == "__main__":
    vals = [22]
    print(calc_max_staircase(vals))
