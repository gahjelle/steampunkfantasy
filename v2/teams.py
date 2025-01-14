import data

ork = data.Race.from_toml("ork")
darkelf = data.Race.from_toml("darkelf")
dwarf = data.Race.from_toml("dwarf")

hss = data.Team("Hss den store")
t = data.Team("Geir Arnes superorker")
t.add_unit(ork.units.grunt, name="Hans Sverre")
t.add_equipment("Hans Sverre", ork.equipments.clockwork_wings)
t.add_unit(ork.units.grunt)
t.add_unit(ork.units.grunt)
t.add_unit(ork.units.grunt)
t.add_unit(ork.units.bioengineered_ork, name="Geir Arne")
t.upgrade_model("Geir Arne", ork.models.elite_bioengineered_ork)
t.upgrade_model("Geir Arne", ork.models.elite_bioengineered_ork)
t.upgrade_model("Geir Arne", ork.models.elite_bioengineered_ork)
t.upgrade_model("Geir Arne", ork.models.elite_bioengineered_ork)
t.add_equipment("Geir Arne", ork.equipments.flame_covered_axe)
t.add_equipment("Geir Arne", ork.equipments.flame_covered_axe)
t.add_equipment("Geir Arne", ork.equipments.flame_covered_axe)
t.add_equipment("Geir Arne", ork.equipments.flame_covered_axe)
beo_1 = t.add_unit(ork.units.bioengineered_ork)
t.upgrade_model(beo_1, ork.models.elite_bioengineered_ork)
t.upgrade_model(beo_1, ork.models.elite_bioengineered_ork)
t.upgrade_model(beo_1, ork.models.elite_bioengineered_ork)
t.upgrade_model(beo_1, ork.models.elite_bioengineered_ork)
t.add_equipment(beo_1, ork.equipments.flame_covered_axe)
t.add_equipment(beo_1, ork.equipments.flame_covered_axe)
t.add_equipment(beo_1, ork.equipments.flame_covered_axe)
t.add_equipment(beo_1, ork.equipments.flame_covered_axe)
beo_2 = t.add_unit(ork.units.bioengineered_ork)
t.upgrade_model(beo_2, ork.models.elite_bioengineered_ork)
t.upgrade_model(beo_2, ork.models.elite_bioengineered_ork)
t.upgrade_model(beo_2, ork.models.elite_bioengineered_ork)
t.upgrade_model(beo_2, ork.models.elite_bioengineered_ork)
beo_3 = t.add_unit(ork.units.bioengineered_ork)
t.upgrade_model(beo_3, ork.models.elite_bioengineered_ork)
t.upgrade_model(beo_3, ork.models.elite_bioengineered_ork)
t.upgrade_model(beo_3, ork.models.elite_bioengineered_ork)
t.upgrade_model(beo_3, ork.models.elite_bioengineered_ork)
