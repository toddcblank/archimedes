from django.db import models

# Create your models here.
class Role:

    MERLIN = 1
    PERCIVAL = 2
    ASSASSIN = 3
    MORDRED = 4
    MORGANA = 5
    OBERON = 6
    GENERIC_GOOD = 7
    GENERIC_BAD = 8
    GOOD_LANCELOT_1 = 9
    EVIL_LANCELOT_1 = 10
    GOOD_LANCELOT_2 = 11
    EVIL_LANCELOT_2 = 12

    ROLE_NAMES = [
        (MERLIN, "Merlin"),
        (PERCIVAL, "Percival"),
        (ASSASSIN, "Assassin"),
        (MORDRED, "Mordred"),
        (MORGANA, "Morgana"),
        (OBERON, "Oberon"),
        (GENERIC_GOOD, "Generic Good Guy"),
        (GENERIC_BAD, "Generic Bad Guy"),
        (GOOD_LANCELOT_1, "Good Lancelot (type 1)"),
        (EVIL_LANCELOT_1, "Evil Lancelot (type 1)"),
        (GOOD_LANCELOT_2, "Good Lancelot (type 2)"),
        (EVIL_LANCELOT_2, "Evil Lancelot (type 2)"),
    ]

    visibleRoles = {
        MERLIN: [ASSASSIN, MORGANA, OBERON, GENERIC_BAD, EVIL_LANCELOT_1, EVIL_LANCELOT_2],
        PERCIVAL: [MERLIN, MORGANA],
        ASSASSIN: [MORDRED, MORGANA, GENERIC_BAD, EVIL_LANCELOT_1, EVIL_LANCELOT_2],
        MORDRED: [ASSASSIN, MORGANA, GENERIC_BAD, EVIL_LANCELOT_1, EVIL_LANCELOT_2],
        MORGANA: [ASSASSIN, MORDRED, GENERIC_BAD, EVIL_LANCELOT_1, EVIL_LANCELOT_2],
        OBERON: [],
        GENERIC_GOOD: [],
        GENERIC_BAD: [ASSASSIN, MORDRED, MORGANA, GENERIC_BAD, EVIL_LANCELOT_1, EVIL_LANCELOT_2],
        GOOD_LANCELOT_1: [],
        EVIL_LANCELOT_1: [ASSASSIN, MORDRED, MORGANA, GENERIC_BAD, EVIL_LANCELOT_1, EVIL_LANCELOT_2],
        GOOD_LANCELOT_2: [EVIL_LANCELOT_2],
        EVIL_LANCELOT_2: [ASSASSIN, MORDRED, MORGANA, GENERIC_BAD, EVIL_LANCELOT_1, GOOD_LANCELOT_2]
    }

class Faction:
    NONE = 0
    GOOD_GUYS = 1
    BAD_GUYS = 2
    FACTIONS = [
        (NONE, "None"),
        (GOOD_GUYS, "Servants of Arthur"),
        (BAD_GUYS, "Minions of Mordred")
    ]


class Game:
    winner = models.IntegerField(default=Faction.NONE, choices=Faction.FACTIONS)
    pass

class MissionResult(models.Model):
    game = models.ForeignKey(Game)
    result = models.IntegerField(default=Faction.NONE, choices=Faction.FACTIONS)

class PlayerRoleForGame(models.Model):
    game = models.ForeignKey(Game)
    playerName = models.CharField(max_length=128)
    role = models.IntegerField(choices=Role.ROLE_NAMES)