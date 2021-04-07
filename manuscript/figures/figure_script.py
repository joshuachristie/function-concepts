# these dependency graphs were combined using inkscape into the manuscript figures
# you can run the script and generate the figures through jupyter lab in docker
# launch the container from the manuscript/figure directory, choose terminal, and type
# python ./figure_script.py
import spacy
nlp = spacy.load("en_core_sci_scibert")

# sentences
eff = nlp("The transcript functions to regulate expression.")
role = nlp("The transcript functions to regulate expression in metabolism.")
adv = nlp("The transcript functions to regulate expression in metabolism by improving glycogen storage.")
sel_eff = nlp("Zebra stripes are functional as they evolved to reduce insect bites.")
to_work = nlp("Liver function benefits human health.")
eff_unsp = nlp("The transcript shows evidence of purifying selection, suggesting that it is functional.")

eff_img = spacy.displacy.render(eff, style="dep", jupyter=False,
                                options={"compact": True, "distance": 120})
role_img = spacy.displacy.render(role, style="dep", jupyter=False,
                                 options={"compact": True, "distance": 100})
adv_img = spacy.displacy.render(adv, style="dep", jupyter=False,
                                options={"compact": True, "distance": 75})
sel_eff_img = spacy.displacy.render(sel_eff, style="dep", jupyter=False,
                                    options={"compact": True, "distance": 65})
to_work_img = spacy.displacy.render(to_work, style="dep", jupyter=False,
                                    options={"compact": True, "distance": 120})
eff_unsp_img = spacy.displacy.render(eff_unsp, style="dep", jupyter=False,
                                     options={"compact": True, "distance": 70})

out_eff = spacy.Path("./eff.svg")
out_role = spacy.Path("./role.svg")
out_adv = spacy.Path("./adv.svg")
out_sel_eff = spacy.Path("./sel_eff.svg")
out_to_work = spacy.Path("./to_work.svg")
out_eff_unsp = spacy.Path("./eff_unsp.svg")

out_eff.open("w", encoding="utf-8").write(eff_img)
out_role.open("w", encoding="utf-8").write(role_img)
out_adv.open("w", encoding="utf-8").write(adv_img)
out_sel_eff.open("w", encoding="utf-8").write(sel_eff_img)
out_to_work.open("w", encoding="utf-8").write(to_work_img)
out_eff_unsp.open("w", encoding="utf-8").write(eff_unsp_img)
