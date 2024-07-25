#slovary
# user, identification number
my_dict = {"bot_qwerty": 45761344 , "begemot321" : 82106439, "sokol1997" : 34509856, "zxc_user": 83407134}
print ("Dict:", my_dict)
print ("Existing value:", my_dict["begemot321"])
print ("Not existing value:", my_dict.get("player"))
my_dict.update({"player" : 79834766,
                "ubivator3000" : 23754981})
a = my_dict.pop("sokol1997")
print ("Deleted value:", a)
print ("Modified dictionary:", my_dict)

print ("             ")

#mogzestva
my_set = {13, "zebra", 13, 13, 12.12, "zebra", "bogomol", 12.12, True}
print ("Set", my_set)
my_set.add("lastochka")
my_set.discard("zebra")
print ("Modified set:", my_set)

