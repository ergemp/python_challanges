def duplicate_array(g_array, g_n_times):
    ret_val = [];
    ctl = 0;

    while ctl < g_n_times:
        ret_val.append(g_array);
        ctl = ctl + 1;

    return ret_val
