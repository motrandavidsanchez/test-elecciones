from .models import Voter, Voting


def has_voted(dni):
    try:
        voter = Voter.objects.get(dni=dni)
        return voter.has_voted
    except Voter.DoesNotExist:
        return None


def has_voted_percentage():
    total_voters = Voter.objects.count()
    voted_voters = Voter.objects.filter(has_voted=True).count()

    if total_voters == 0:
        return 0

    return (voted_voters / total_voters) * 100


def all_voting_false():
    return not Voting.objects.filter(voting=True).exists()


def all_voting_false_percentage():
    total_establishment = Voting.objects.count()
    total_voting_false = Voting.objects.filter(voting=False).count()
    return (total_voting_false / total_establishment) * 100 if total_voting_false != 0 else 0
