from flask import Flask, request, render_template
import openai

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def monster_maker():
    error = None
    if request.method == "GET":
        return render_template("maker_form.html")
    elif request.method == "POST":
        openai.api_key = "YOUR_CODE_HERE"
        completion = openai.Completion.create(
            engine="text-davinci-002",
            prompt="Create a statblock for these D&D 5e monsters \n\nDire Wolf\nLarge beast, unaligned\nArmor Class: 14 (Natural Armor)\nHit Points: 37 (5d10+10)\nSpeed: 50ft\nSTR: 17 (+3)\nDEX: 15 (+2)\nCON: 15 (+2)\nINT: 10 (+0)\nWIS: 12 (+1)\nCHA: 7 (-2)\nSkills: Perception +3, Stealth +4\nSenses: passive Perception 13\nLanguages: None\nChallenge: 1 (200 XP)\nAbilities:\nKeen Hearing and Smell: The wolf has advantage on Wisdom (Perception) checks that rely on hearing or smell.\nPack Tactics: The wolf has advantage on an attack roll against a creature if at least one of the wolf's allies is within 5 ft. of the creature and the ally isn't incapacitated.\nActions\nBite: Melee Weapon Attack: +5 to hit, reach 5ft., one target. Hit: (2d6+3) piercing damage. If the target is a creature, it must succeed on a DC 13 Strength saving throw or be knocked prone.\n\n" + request.form["monster_name"],
            max_tokens=500
        )
        text = completion["choices"][0]["text"]
        lines = [line for line in text.split("\n") if line != ""]

        try:
            monster_type = lines[0].split(", ")[0]
        except:
            monster_type

        try:
            alignment = lines[0].split(", ")[1]
        except IndexError:
            alignment = "ERROR"
        try:
            armor = [line.split(": ")[1] for line in lines if "armor class" in line.lower() or "AC" in line][0]
        except IndexError:
            armor = "ERROR"
        try:
            hp = [line.split(": ")[1] for line in lines if "hit points" in line.lower() or "hp" in line.lower()][0]
        except IndexError:
            hp = "ERROR"

        try:
            speed = [line.split(": ")[1] for line in lines if "Speed" in line][0]
        except IndexError:
            speed = "ERROR"

        try:
            strength = [line.split(": ")[1] for line in lines if "STR" in line][0]
        except IndexError:
            strength = "ERROR"

        try:
            dexterity = [line.split(": ")[1] for line in lines if "DEX" in line][0]
        except IndexError:
            dexterity = "ERROR"

        try:
            constitution = [line.split(": ")[1] for line in lines if "CON" in line][0]
        except IndexError:
            constitution = "ERROR"

        try:
            intelligence = [line.split(": ")[1] for line in lines if "INT" in line][0]
        except IndexError:
            intelligence = "ERROR"

        try:
            wisdom = [line.split(": ")[1] for line in lines if "WIS" in line][0]
        except IndexError:
            wisdom = "ERROR"

        try:
            charisma = [line.split(": ")[1] for line in lines if "CHA" in line][0]
        except IndexError:
            charisma = "ERROR"

        try:
            saving_throws = [line.split(": ")[1] for line in lines if "saving throws" in line.lower() or "saves" in line.lower()][0]
        except IndexError:
            saving_throws = "ERROR"

        try:
            skills = [line.split(": ")[1] for line in lines if "skills" in line.lower()][0]
        except IndexError:
            skills = "ERROR"

        try:
            senses = [line.split(": ")[1] for line in lines if "Senses" in line][0]
        except IndexError:
            senses = "ERROR"

        try:
            languages = [line.split(": ")[1] for line in lines if "Languages" in line][0]
        except IndexError:
            languages = "ERROR"

        try:
            challenge = [line.split(": ")[1] for line in lines if "challenge" in line.lower() or "CR" in line][0]
        except IndexError:
            challenge = "ERROR"

        try:
            raw_abilities = lines[[idx for idx, s in enumerate(lines) if "challenge" in s.lower()][0]+1:(lines.index("Actions"))]
            abilities = [(ability.split(".", 1)) for ability in raw_abilities]
        except:
            abilities = ["ERROR"]

        try:
            raw_actions = lines[(lines.index("Actions"))+1:]
            print(raw_actions)
            actions = [(action.split(":", 1)) for action in raw_actions]
            print(actions)
        except:
            actions = ["ERROR"]

        return render_template("statblock.html",
                               monster_name = request.form["monster_name"],
                               monster_type = monster_type,
                               alignment = alignment,
                               armor = armor,
                               hp = hp,
                               speed = speed,
                               strength = strength,
                               dexterity = dexterity,
                               constitution = constitution,
                               intelligence = intelligence,
                               wisdom = wisdom,
                               charisma = charisma,
                               saving_throws = saving_throws,
                               skills = skills,
                               # immunities = immunities,
                               senses = senses,
                               languages = languages,
                               challenge = challenge,
                               abilities = abilities,
                               actions = actions,
                               raw = completion["choices"][0]["text"]
                               )
    else:
        return "Test test test test test"

if __name__ == '__main__':
    app.run()
