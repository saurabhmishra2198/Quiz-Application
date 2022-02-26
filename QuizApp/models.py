from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

# Home page model 
class Python(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class Java(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class OOPC(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class C(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class DBMS(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class HTML(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     # 3  db_table="QuizApp"
    def __str__(self):
        return self.Question

class ComputerNetwork(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
      #  db_table="QuizApp"
    def __str__(self):
        return self.Question

class Bootstrap(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class DataStructure(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question
    
# Gk model

class BasicGK(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class Technology(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class IndianHistory(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class HonoursAward(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class GeneralScience(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class BookAuthor(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class FamousPersonalities(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class IndianCulture(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class IndianPolitics(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class Sports(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class WorldGeography(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class WorldOrganisations(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class IndianEconomy(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class IndianGeography(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class Inventions(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class FamousPlaceIndia(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

# Aptitude models
class ProblemTrains(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class PermutationCombination(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class TimeDistance(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class HCFAndLCM(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class SimpleInterest(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class DecimalFraction(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class CompoundInterest(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class SquareCubeRoot(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class ProfitLoss(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class Simplification(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class Partnership(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class RatioProportion(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class ProblemAge(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class PipesCistern(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class VolumeSurfaceArea(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class RacesGame(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

# Logical Model
class NumberSeries(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class StatementAssumption(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class LetterSymbol(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class CourceAction(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class VerbalClassification(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class StatementConClusion(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class Artificial(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class ThemeDetection(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class VerbalReasoning(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class CauseEffect(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class LogicalProblem(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class StatementArgument(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class LogicalGame(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class LogicalDeduction(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class AnalyzingArgument(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class EssentialPart(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

# Current-Affairs models
class State(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class AwardHonour(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class Politics(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class Banking(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class National(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class BillsActs(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class Persons(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class Business(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class International(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class Defence(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class importantDay(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class Economy(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class Agriculture(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class Education(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class ArtCulture(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class Environment(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

#Science
class Science(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class Kinematics(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class Physics(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class Electrostatics(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class Chemistry(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class OrganicChemistry(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class Biology(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class ChemicalThermodynamics(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class Mathematics(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class ChemicalKinetics(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class English(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class PlantPhysiology(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class Thermodynamics(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class HumanPhysiology(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question
    
class ElectromagneticWaves(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class BiotechnologyApplication(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

#Interview models
class PlacementPapers(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class HRInterview(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class TechnicalInterview(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class GroupDisCussion(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class SubmitYourPlacement(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class BodyLanguage(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

#Online Test models
class AptitudeTest(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class BiotechnologyTest(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class VerbalAbilityTest(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class BiochemicalEngineering(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class LogicalReasoning(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class DigitalElectronics(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class NonVerbalReasoning(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class Electronics(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class DataInterpretation(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class ChemicalEngineering(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class GeneralKnowledge(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class NetworkingTest(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class CurrentAffairsTest(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class ComputerScienceTest(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class MicrobiologyTest(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class C_ShapProgramming(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

#Varbal Models
class SpottingError(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class SentenceImprovement(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class Synonyms(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class CompletingStatement(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class Antonyms(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class OrderingSentences(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class SelectingWord(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class ParagraphFormation(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class Spelling(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class ClostTest(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class SentenceFormation(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class Comprehension(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class OrderingWord(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class OneWordSubstitutes(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class SentenceCorrection(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class IdiomsPhrases(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

#Engineering Models
class ComputerScience(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class Chemical(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class Civil(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class Electrical(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class Structural(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question

class Mechanical(models.Model):
    Question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctans = models.CharField(max_length=100)
    #class Meta:
     #   db_table="QuizApp"
    def __str__(self):
        return self.Question


#