from django.contrib import admin
from QuizApp.models import Contact
# Home model
from QuizApp.models import Python,Java,OOPC,C,DBMS,HTML,ComputerNetwork,Bootstrap,DataStructure
#Gk model
from QuizApp.models import BasicGK,Technology,IndianHistory,HonoursAward,GeneralScience,BookAuthor,FamousPersonalities
from QuizApp.models import IndianCulture,IndianPolitics,Sports,WorldGeography,WorldOrganisations,IndianEconomy,IndianGeography,Inventions,FamousPlaceIndia
#Aptitude model
from QuizApp.models import ProblemTrains,PermutationCombination,TimeDistance,HCFAndLCM,SimpleInterest,DecimalFraction,CompoundInterest,SquareCubeRoot,ProfitLoss
from QuizApp.models import Simplification,Partnership,RatioProportion,ProblemAge,PipesCistern,VolumeSurfaceArea,RacesGame
#Logical model
from QuizApp.models import NumberSeries,StatementAssumption,LetterSymbol,CourceAction,VerbalClassification,StatementConClusion,Artificial,ThemeDetection,VerbalReasoning
from QuizApp.models import CauseEffect,LogicalProblem,StatementArgument,LogicalGame,LogicalDeduction,AnalyzingArgument,EssentialPart
#Current_Affair
from QuizApp.models import State,AwardHonour,Politics,Banking,National,BillsActs,Persons,Business,International
from QuizApp.models import Defence,importantDay,Economy,Agriculture,Education,ArtCulture,Environment
#Science 
from QuizApp.models import Science,Kinematics,Physics,Electrostatics,Chemistry,OrganicChemistry,Biology,ChemicalThermodynamics
from QuizApp.models import Mathematics,ChemicalKinetics,English,PlantPhysiology,Thermodynamics,HumanPhysiology,ElectromagneticWaves,BiotechnologyApplication
#Interview
from QuizApp.models import PlacementPapers,HRInterview,TechnicalInterview,GroupDisCussion,SubmitYourPlacement,BodyLanguage
#Online-Test
from QuizApp.models import AptitudeTest,BiotechnologyTest,VerbalAbilityTest,BiochemicalEngineering,LogicalReasoning,DigitalElectronics,NonVerbalReasoning,Electronics,DataInterpretation
from QuizApp.models import ChemicalEngineering,GeneralKnowledge,NetworkingTest,CurrentAffairsTest,ComputerScienceTest,MicrobiologyTest,C_ShapProgramming
#Varbal 
from QuizApp.models import SpottingError,SentenceImprovement,Synonyms,CompletingStatement,Antonyms,OrderingSentences,SelectingWord,ParagraphFormation,Spelling,ClostTest,SentenceFormation
from QuizApp.models import Comprehension,OrderingWord,OneWordSubstitutes,SentenceCorrection,IdiomsPhrases
#Engineering
from QuizApp.models import ComputerScience,Civil,Chemical,Mechanical,Structural,Electrical

# Register your models here.
admin.site.register(Contact)
# Home page models
admin.site.register(Python)
admin.site.register(Java)
admin.site.register(OOPC)
admin.site.register(C)
admin.site.register(DBMS)
admin.site.register(HTML)
admin.site.register(ComputerNetwork)
admin.site.register(Bootstrap)
admin.site.register(DataStructure)
# Gk page models
admin.site.register(BasicGK)
admin.site.register(Technology)
admin.site.register(IndianHistory)
admin.site.register(HonoursAward)
admin.site.register(GeneralScience)
admin.site.register(BookAuthor)
admin.site.register(FamousPersonalities)
admin.site.register(IndianCulture)
admin.site.register(IndianPolitics)
admin.site.register(Sports)
admin.site.register(WorldGeography)
admin.site.register(WorldOrganisations)
admin.site.register(IndianEconomy)
admin.site.register(IndianGeography)
admin.site.register(Inventions)
admin.site.register(FamousPlaceIndia)

# Aptitude models
admin.site.register(ProblemTrains)
admin.site.register(PermutationCombination)
admin.site.register(TimeDistance)
admin.site.register(HCFAndLCM)
admin.site.register(SimpleInterest)
admin.site.register(DecimalFraction)
admin.site.register(CompoundInterest)
admin.site.register(SquareCubeRoot)
admin.site.register(ProfitLoss)
admin.site.register(Simplification)
admin.site.register(Partnership)
admin.site.register(RatioProportion)
admin.site.register(ProblemAge)
admin.site.register(PipesCistern)
admin.site.register(VolumeSurfaceArea)
admin.site.register(RacesGame)

#Logical model
admin.site.register(NumberSeries)
admin.site.register(StatementAssumption)
admin.site.register(LetterSymbol)
admin.site.register(CourceAction)
admin.site.register(VerbalClassification)
admin.site.register(StatementConClusion)
admin.site.register(Artificial)
admin.site.register(ThemeDetection)
admin.site.register(VerbalReasoning)
admin.site.register(CauseEffect)
admin.site.register(LogicalProblem)
admin.site.register(StatementArgument)
admin.site.register(LogicalGame)
admin.site.register(LogicalDeduction)
admin.site.register(AnalyzingArgument)
admin.site.register(EssentialPart)

#Current-Affairs models
admin.site.register(State)
admin.site.register(AwardHonour)
admin.site.register(Politics)
admin.site.register(Banking)
admin.site.register(National)
admin.site.register(BillsActs)
admin.site.register(Persons)
admin.site.register(Business)
admin.site.register(International)
admin.site.register(Defence)
admin.site.register(importantDay)
admin.site.register(Economy)
admin.site.register(Agriculture)
admin.site.register(Education)
admin.site.register(ArtCulture)
admin.site.register(Environment)

#Science model
admin.site.register(Science)
admin.site.register(Kinematics)
admin.site.register(Physics)
admin.site.register(Electrostatics)
admin.site.register(Chemistry)
admin.site.register(OrganicChemistry)
admin.site.register(Biology)
admin.site.register(ChemicalThermodynamics)
admin.site.register(Mathematics)
admin.site.register(ChemicalKinetics)
admin.site.register(English)
admin.site.register(PlantPhysiology)
admin.site.register(Thermodynamics)
admin.site.register(HumanPhysiology)
admin.site.register(ElectromagneticWaves)
admin.site.register(BiotechnologyApplication)

#Interview admin
admin.site.register(PlacementPapers)
admin.site.register(HRInterview)
admin.site.register(TechnicalInterview)
admin.site.register(GroupDisCussion)
admin.site.register(SubmitYourPlacement)
admin.site.register(BodyLanguage)

#Online Test admin
admin.site.register(AptitudeTest)
admin.site.register(BiotechnologyTest)
admin.site.register(VerbalAbilityTest)
admin.site.register(BiochemicalEngineering)
admin.site.register(LogicalReasoning)
admin.site.register(DigitalElectronics)
admin.site.register(NonVerbalReasoning)
admin.site.register(Electronics)
admin.site.register(DataInterpretation)
admin.site.register(ChemicalEngineering)
admin.site.register(GeneralKnowledge)
admin.site.register(NetworkingTest)
admin.site.register(CurrentAffairsTest)
admin.site.register(ComputerScienceTest)
admin.site.register(MicrobiologyTest)
admin.site.register(C_ShapProgramming)

#Varbal admin
admin.site.register(SpottingError)
admin.site.register(SentenceImprovement)
admin.site.register(Synonyms)
admin.site.register(CompletingStatement)
admin.site.register(Antonyms)
admin.site.register(OrderingSentences)
admin.site.register(SelectingWord)
admin.site.register(ParagraphFormation)
admin.site.register(Spelling)
admin.site.register(ClostTest)
admin.site.register(SentenceFormation)
admin.site.register(Comprehension)
admin.site.register(OrderingWord)
admin.site.register(OneWordSubstitutes)
admin.site.register(SentenceCorrection)
admin.site.register(IdiomsPhrases)

#Engineering admin
admin.site.register(ComputerScience)
admin.site.register(Chemical)
admin.site.register(Civil)
admin.site.register(Mechanical)
admin.site.register(Structural)
admin.site.register(Electrical)

#