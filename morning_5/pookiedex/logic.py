from flask import current_app


def query(form):
    print(form)
    result = []
    for pokemon in current_app.config["data"]:
        if pokemon["Primary Typing"] != form["primary_typing"]:
            if form["primary_typing"] != "any":
                continue
        if pokemon["Secondary Typing"] != form["secondary_typing"]:
            if form["secondary_typing"] != "any":
                continue
        if pokemon["Generation"] != form["generation"]:
            if form["generation"] != "any":
                continue
        if form.get("legendary_only", "off") == "on":
            if pokemon["Legendary Status"] != "True":
                continue
        if form.get("min_total", "").isdigit():
            min_total_stats = int(form.get("min_total"))
        else:
            min_total_stats = 0
        if form.get("max_total", "").isdigit():
            max_total_stats = int(form.get("max_total"))
        else:
            max_total_stats = 1000
        if int(pokemon["Base Stat Total"]) not in range(min_total_stats, max_total_stats + 1):
            continue
        result.append(pokemon)
    return result
