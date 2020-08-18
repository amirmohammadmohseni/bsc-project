from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.student.id, filename)


class Proposal(models.Model):
    title = models.CharField(max_length=60)
    titlePersian = models.CharField(max_length=60)

    student = models.ForeignKey('users.Student', on_delete=models.SET_NULL, null=True)

    arbiter1 = models.ForeignKey('users.Professor', on_delete=models.SET_NULL, null=True, related_name='arbiter1')
    arbiter2 = models.ForeignKey('users.Professor', on_delete=models.SET_NULL, null=True, related_name='arbiter2')

    issuanceDate = models.DateTimeField(auto_now_add=True, auto_now=False)

    keywords = models.TextField()    # Array Field? Or OneToMany Relationship?

    class ResearchType(models.TextChoices):
        FUNDAMENTAL = 'FU', _('Fundamental')
        THEORETICAL = 'TH', _('Theoretical')
        PRACTICAL = 'PR', _('Practical')
        DEVELOPMENTAL = 'DE', _('Developmental')

    # This Should be changed to a Multiple choice field!
    researchType = models.CharField(
        max_length=2,
        choices=ResearchType.choices,
        default=ResearchType.FUNDAMENTAL,
    )

    defenseDate = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    councilApproved = models.BooleanField(default=False)

    file = models.FileField(upload_to=user_directory_path)

    tarifMasale = models.TextField(max_length=5000)
    pishinehPazhuhesh = models.TextField(max_length=5000)
    ruykardHal = models.TextField(max_length=5000)
    premises = models.TextField(max_length=5000)
    jadidBudan = models.TextField(max_length=5000)
    raveshVaAbzar = models.TextField(max_length=5000)
    marajeHami = models.TextField(max_length=5000)

    class Meta:
        verbose_name = _('proposal')
        verbose_name_plural = _('proposals')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('proposal_detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    author = models.ForeignKey('users.Professor', on_delete=models.SET_NULL, null=True)

    onProposal = models.ForeignKey('Proposal', on_delete=models.SET_NULL, null=True)

    context = models.TextField(max_length=5000)

    createdAt = models.DateTimeField(auto_now=False)

    class CommentType(models.TextChoices):
        REVISION = 'RE', _('Revision')
        DEFENSE = 'DE', _('Defense')

    commentOn = models.CharField(max_length=2, choices=CommentType.choices, default=CommentType.REVISION)

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')

    def __str__(self):
        return "Comment On " + self.onProposal.title

    def get_absolute_url(self):
        return reverse('comment_detail', kwargs={'pk': self.pk})


class ProposalSubmission(models.Model):
    title = models.CharField(max_length=25)

    openAt = models.DateTimeField(auto_now=False, auto_now_add=False)
    closeAt = models.DateTimeField(auto_now=False, auto_now_add=False)

    revisionUntil = models.DateTimeField(auto_now=False, auto_now_add=False)

    semester = models.PositiveIntegerField()

    class Meta:
        verbose_name = _('proposalsubmission')
        verbose_name_plural = _('proposalsubmissions')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('proposalsubmission_detail', kwargs={'pk': self.pk})
