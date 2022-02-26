from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from QuizApp.models import Contact,Python
from QuizApp.models import Java,OOPC,C,DBMS,HTML,ComputerNetwork,Bootstrap,DataStructure
# Gk model
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

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .Forms import UserRegisterForm



# Create your views here.
def registerUser(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account create for {username}!')
            return redirect('/home')
    else:
        form = UserRegisterForm()
    return render(request, "register.html",{'form':form})
    #return render(request,'register.html')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect('/home')
        else:
            # No backend authenticated the credentials
            return render(request,'login.html')
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')

def index(request):
    return render(request,'index.html')

def home(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been send!')
    return render(request,'contact.html')

#Home page
def python(request):
    results = Python.objects.all()
    return render(request,'python.html',{'Python':results})

def java(request):
    results = Java.objects.all()
    return render(request,'java.html',{'Java':results})

def oopc(request):
    results = OOPC.objects.all()
    return render(request,'c++.html',{'OOPC':results})

def c(request):
    results = C.objects.all()
    return render(request,'c.html',{'C':results})

def dbms(request):
    results = DBMS.objects.all()
    return render(request,'dbms.html',{'DBMS':results})

def html(request):
    results = HTML.objects.all()
    return render(request,'html.html',{'HTML':results})

def network(request):
    results = ComputerNetwork.objects.all()
    return render(request,'network.html',{'ComputerNetwork':results})

def bootstrap(request):
    results = Bootstrap.objects.all()
    return render(request,'bootstrap.html',{'Bootstrap':results})

def datastructure(request):
    results = DataStructure.objects.all()
    return render(request,'datastructure.html',{'DataStructure':results})

#Second nav-bar
def GK(request):
    return render(request,'GK.html')

def aptitude(request):
    return render(request,'aptitude.html')

def logical(request):
    return render(request,'logical.html')

def current_affair(request):
    return render(request,'current_affair.html')

def science(request):
    return render(request,'science.html')

def interview(request):
    return render(request,'interview.html')

def online_test(request):
    return render(request,'online_test.html')

def varbal(request):
    return render(request,'varbal.html')

def engineering(request):
    return render(request,'engineering.html')

#search bar
def search(request):
    return render(request,'search.html')

#Facality Bar
def blog(request):
    return render(request,'blog.html')

# Gk Views

def basicGK(request):
    results = BasicGK.objects.all()
    return render(request,'basicGk.html',{'BasicGK':results})

def technology(request):
    results = Technology.objects.all()
    return render(request,'technology.html',{'Technology':results})

def indianHistory(request):
    results = IndianHistory.objects.all()
    return render(request,'IndianHistory.html',{'IndianHistory':results})

def honoursAward(request):
    results = HonoursAward.objects.all()
    return render(request,'HonoursAward.html',{'HonoursAward':results})

def generalScience(request):
    results = GeneralScience.objects.all()
    return render(request,'GeneralScience.html',{'GeneralScience':results})

def bookAuthor(request):
    results = BookAuthor.objects.all()
    return render(request,'BookAuthor.html',{'BookAuthor':results})

def famousPersonalities(request):
    results = FamousPersonalities.objects.all()
    return render(request,'FamousPersonalities.html',{'FamousPersonalities':results})

def indianCulture(request):
    results = IndianCulture.objects.all()
    return render(request,'IndianCulture.html',{'IndianCulture':results})

def indianPolitics(request):
    results = IndianPolitics.objects.all()
    return render(request,'IndianPolitics.html',{'IndianPolitics':results})

def sports(request):
    results = Sports.objects.all()
    return render(request,'Sports.html',{'Sports':results})

def worldGeography(request):
    results = WorldGeography.objects.all()
    return render(request,'WorldGeography.html',{'WorldGeography':results})

def worldOrganisations(request):
    results = WorldOrganisations.objects.all()
    return render(request,'WorldOrganisations.html',{'WorldOrganisations':results})

def indianEconomy(request):
    results = IndianEconomy.objects.all()
    return render(request,'IndianEconomy.html',{'IndianEconomy':results})

def indianGeography(request):
    results = IndianGeography.objects.all()
    return render(request,'IndianGeography.html',{'IndianGeography':results})

def inventions(request):
    results = Inventions.objects.all()
    return render(request,'Inventions.html',{'Inventions':results})

def famousPlaceIndia(request):
    results = FamousPlaceIndia.objects.all()
    return render(request,'FamousPlaceIndia.html',{'FamousPlaceIndia':results})

# Aptitude Views
def problemTrains(request):
    results = ProblemTrains.objects.all()
    return render(request,'ProblemTrains.html',{'ProblemTrains':results})

def permutationCombination(request):
    results = PermutationCombination.objects.all()
    return render(request,'PermutationCombination.html',{'PermutationCombination':results})

def timeDistance(request):
    results = TimeDistance.objects.all()
    return render(request,'TimeDistance.html',{'TimeDistance':results})

def hCFAndLCM(request):
    results = HCFAndLCM.objects.all()
    return render(request,'HCFAndLCM.html',{'HCFAndLCM':results})

def simpleInterest(request):
    results = SimpleInterest.objects.all()
    return render(request,'SimpleInterest.html',{'SimpleInterest':results})

def decimalFraction(request):
    results = DecimalFraction.objects.all()
    return render(request,'DecimalFraction.html',{'DecimalFraction':results})

def compoundInterest(request):
    results = CompoundInterest.objects.all()
    return render(request,'CompoundInterest.html',{'CompoundInterest':results})

def squareCubeRoot(request):
    results = SquareCubeRoot.objects.all()
    return render(request,'SquareCubeRoot.html',{'SquareCubeRoot':results})

def profitLoss(request):
    results = ProfitLoss.objects.all()
    return render(request,'ProfitLoss.html',{'ProfitLoss':results})

def simplification(request):
    results = Simplification.objects.all()
    return render(request,'Simplification.html',{'Simplification':results})

def partnership(request):
    results = Partnership.objects.all()
    return render(request,'Partnership.html',{'Partnership':results})

def ratioProportion(request):
    results = RatioProportion.objects.all()
    return render(request,'RatioProportion.html',{'RatioProportion':results})

def problemAge(request):
    results = ProblemAge.objects.all()
    return render(request,'ProblemAge.html',{'ProblemAge':results})

def pipesCistern(request):
    results = PipesCistern.objects.all()
    return render(request,'PipesCistern.html',{'PipesCistern':results})

def volumeSurfaceArea(request):
    results = VolumeSurfaceArea.objects.all()
    return render(request,'VolumeSurfaceArea.html',{'VolumeSurfaceArea':results})

def racesGame(request):
    results = RacesGame.objects.all()
    return render(request,'RacesGame.html',{'RacesGame':results})

#Logical Views
def numberSeries(request):
    results = NumberSeries.objects.all()
    return render(request,'NumberSeries.html',{'NumberSeries':results})

def statementAssumption(request):
    results = StatementAssumption.objects.all()
    return render(request,'StatementAssumption.html',{'StatementAssumption':results})

def letterSymbol(request):
    results = LetterSymbol.objects.all()
    return render(request,'LetterSymbol.html',{'LetterSymbol':results})

def courceAction(request):
    results = CourceAction.objects.all()
    return render(request,'CourceAction.html',{'CourceAction':results})

def verbalClassification(request):
    results = VerbalClassification.objects.all()
    return render(request,'VerbalClassification.html',{'VerbalClassification':results})

def statementConClusion(request):
    results = StatementConClusion.objects.all()
    return render(request,'StatementConClusion.html',{'StatementConClusion':results})

def artificial(request):
    results = Artificial.objects.all()
    return render(request,'Artificial.html',{'Artificial':results})

def themeDetection(request):
    results = ThemeDetection.objects.all()
    return render(request,'ThemeDetection.html',{'ThemeDetection':results})

def verbalReasoning(request):
    results = VerbalReasoning.objects.all()
    return render(request,'VerbalReasoning.html',{'VerbalReasoning':results})

def causeEffect(request):
    results = CauseEffect.objects.all()
    return render(request,'CauseEffect.html',{'CauseEffect':results})

def logicalProblem(request):
    results = LogicalProblem.objects.all()
    return render(request,'LogicalProblem.html',{'LogicalProblem':results})

def statementArgument(request):
    results = StatementArgument.objects.all()
    return render(request,'StatementArgument.html',{'StatementArgument':results})

def logicalGame(request):
    results = LogicalGame.objects.all()
    return render(request,'LogicalGame.html',{'LogicalGame':results})

def logicalDeduction(request):
    results = LogicalDeduction.objects.all()
    return render(request,'LogicalDeduction.html',{'LogicalDeduction':results})

def analyzingArgument(request):
    results = AnalyzingArgument.objects.all()
    return render(request,'AnalyzingArgument.html',{'AnalyzingArgument':results})

def essentialPart(request):
    results = EssentialPart.objects.all()
    return render(request,'EssentialPart.html',{'EssentialPart':results})

#Current-Affairs views
def state(request):
    results = State.objects.all()
    return render(request,'State.html',{'State':results})

def awardHonour(request):
    results = AwardHonour.objects.all()
    return render(request,'AwardHonour.html',{'AwardHonour':results})

def politics(request):
    results = Politics.objects.all()
    return render(request,'Politics.html',{'Politics':results})

def banking(request):
    results = Banking.objects.all()
    return render(request,'Banking.html',{'Banking':results})

def national(request):
    results = National.objects.all()
    return render(request,'National.html',{'National':results})

def billsActs(request):
    results = BillsActs.objects.all()
    return render(request,'BillsActs.html',{'BillsActs':results})

def persons(request):
    results = Persons.objects.all()
    return render(request,'Persons.html',{'Persons':results})

def business(request):
    results = Business.objects.all()
    return render(request,'Business.html',{'Business':results})

def international(request):
    results = International.objects.all()
    return render(request,'International.html',{'International':results})

def defence(request):
    results = Defence.objects.all()
    return render(request,'Defence.html',{'Defence':results})

def ImportantDay(request):
    results = importantDay.objects.all()
    return render(request,'importantDay.html',{'importantDay':results})

def economy(request):
    results = Economy.objects.all()
    return render(request,'Economy.html',{'Economy':results})

def agriculture(request):
    results = Agriculture.objects.all()
    return render(request,'Agriculture.html',{'Agriculture':results})

def education(request):
    results = Education.objects.all()
    return render(request,'Education.html',{'Education':results})

def artCulture(request):
    results = ArtCulture.objects.all()
    return render(request,'ArtCulture.html',{'ArtCulture':results})

def environment(request):
    results = Environment.objects.all()
    return render(request,'Environment.html',{'Environment':results})

#Science Views
def BasicScience(request):
    results = Science.objects.all()
    return render(request,'BasicScience.html',{'Science':results})

def kinematics(request):
    results = Kinematics.objects.all()
    return render(request,'Kinematics.html',{'Kinematics':results})

def physics(request):
    results = Physics.objects.all()
    return render(request,'Physics.html',{'Physics':results})

def electrostatics(request):
    results = Electrostatics.objects.all()
    return render(request,'Electrostatics.html',{'Electrostatics':results})

def chemistry(request):
    results = Chemistry.objects.all()
    return render(request,'Chemistry.html',{'Chemistry':results})

def organicChemistry(request):
    results = OrganicChemistry.objects.all()
    return render(request,'OrganicChemistry.html',{'OrganicChemistry':results})

def biology(request):
    results = Biology.objects.all()
    return render(request,'Biology.html',{'Biology':results})

def chemicalThermodynamics(request):
    results = ChemicalThermodynamics.objects.all()
    return render(request,'ChemicalThermodynamics.html',{'ChemicalThermodynamics':results})

def mathematics(request):
    results = Mathematics.objects.all()
    return render(request,'Mathematics.html',{'Mathematics':results})

def chemicalKinetics(request):
    results = ChemicalKinetics.objects.all()
    return render(request,'ChemicalKinetics.html',{'ChemicalKinetics':results})

def english(request):
    results = English.objects.all()
    return render(request,'English.html',{'English':results})

def plantPhysiology(request):
    results = PlantPhysiology.objects.all()
    return render(request,'PlantPhysiology.html',{'PlantPhysiology':results})

def thermodynamics(request):
    results = Thermodynamics.objects.all()
    return render(request,'Thermodynamics.html',{'Thermodynamics':results})

def humanPhysiology(request):
    results = HumanPhysiology.objects.all()
    return render(request,'HumanPhysiology.html',{'HumanPhysiology':results})

def electromagneticWaves(request):
    results = ElectromagneticWaves.objects.all()
    return render(request,'ElectromagneticWaves.html',{'ElectromagneticWaves':results})

def biotechnologyApplication(request):
    results = BiotechnologyApplication.objects.all()
    return render(request,'BiotechnologyApplication.html',{'BiotechnologyApplication':results})

#Interview Views
def placementPapers(request):
    results = PlacementPapers.objects.all()
    return render(request,'PlacementPapers.html',{'PlacementPapers':results})

def hRInterview(request):
    results = HRInterview.objects.all()
    return render(request,'HRInterview.html',{'HRInterview':results})

def technicalInterview(request):
    results = TechnicalInterview.objects.all()
    return render(request,'TechnicalInterview.html',{'TechnicalInterview':results})

def groupDisCussion(request):
    results = GroupDisCussion.objects.all()
    return render(request,'GroupDisCussion.html',{'GroupDisCussion':results})

def submitYourPlacement(request):
    results = SubmitYourPlacement.objects.all()
    return render(request,'SubmitYourPlacement.html',{'SubmitYourPlacement':results})

def bodyLanguage(request):
    results = BodyLanguage.objects.all()
    return render(request,'BodyLanguage.html',{'BodyLanguage':results})

#Online Test Views
def aptitudeTest(request):
    results = AptitudeTest.objects.all()
    return render(request,'AptitudeTest.html',{'AptitudeTest':results})

def biotechnologyTest(request):
    results = BiotechnologyTest.objects.all()
    return render(request,'BiotechnologyTest.html',{'BiotechnologyTest':results})

def verbalAbilityTest(request):
    results = VerbalAbilityTest.objects.all()
    return render(request,'VerbalAbilityTest.html',{'VerbalAbilityTest':results})

def biochemicalEngineering(request):
    results = BiochemicalEngineering.objects.all()
    return render(request,'BiochemicalEngineering.html',{'BiochemicalEngineering':results})

def logicalReasoning(request):
    results = LogicalReasoning.objects.all()
    return render(request,'LogicalReasoning.html',{'LogicalReasoning':results})

def digitalElectronics(request):
    results = DigitalElectronics.objects.all()
    return render(request,'DigitalElectronics.html',{'DigitalElectronics':results})

def nonVerbalReasoning(request):
    results = NonVerbalReasoning.objects.all()
    return render(request,'NonVerbalReasoning.html',{'NonVerbalReasoning':results})

def electronics(request):
    results = Electronics.objects.all()
    return render(request,'Electronics.html',{'Electronics':results})

def dataInterpretation(request):
    results = DataInterpretation.objects.all()
    return render(request,'DataInterpretation.html',{'DataInterpretation':results})

def chemicalEngineering(request):
    results = ChemicalEngineering.objects.all()
    return render(request,'ChemicalEngineering.html',{'ChemicalEngineering':results})

def generalKnowledge(request):
    results = GeneralKnowledge.objects.all()
    return render(request,'GeneralKnowledge.html',{'GeneralKnowledge':results})

def networkingTest(request):
    results = NetworkingTest.objects.all()
    return render(request,'NetworkingTest.html',{'NetworkingTest':results})

def currentAffairsTest(request):
    results = CurrentAffairsTest.objects.all()
    return render(request,'CurrentAffairsTest.html',{'CurrentAffairsTest':results})

def computerScienceTest(request):
    results = ComputerScienceTest.objects.all()
    return render(request,'ComputerScienceTest.html',{'ComputerScienceTest':results})

def microbiologyTest(request):
    results = MicrobiologyTest.objects.all()
    return render(request,'MicrobiologyTest.html',{'MicrobiologyTest':results})

def c_ShapProgramming(request):
    results = C_ShapProgramming.objects.all()
    return render(request,'C_ShapProgramming.html',{'C_ShapProgramming':results})

#Varbal Views
def spottingError(request):
    results = SpottingError.objects.all()
    return render(request,'SpottingError.html',{'SpottingError':results})

def sentenceImprovement(request):
    results = SentenceImprovement.objects.all()
    return render(request,'SentenceImprovement.html',{'SentenceImprovement':results})

def synonyms(request):
    results = Synonyms.objects.all()
    return render(request,'Synonyms.html',{'Synonyms':results})

def completingStatement(request):
    results = CompletingStatement.objects.all()
    return render(request,'CompletingStatement.html',{'CompletingStatement':results})

def antonyms(request):
    results = Antonyms.objects.all()
    return render(request,'Antonyms.html',{'Antonyms':results})

def orderingSentences(request):
    results = OrderingSentences.objects.all()
    return render(request,'OrderingSentences.html',{'OrderingSentences':results})

def selectingWord(request):
    results = SelectingWord.objects.all()
    return render(request,'SelectingWord.html',{'SelectingWord':results})

def paragraphFormation(request):
    results = ParagraphFormation.objects.all()
    return render(request,'ParagraphFormation.html',{'ParagraphFormation':results})

def spelling(request):
    results = Spelling.objects.all()
    return render(request,'Spelling.html',{'Spelling':results})

def clostTest(request):
    results = ClostTest.objects.all()
    return render(request,'ClostTest.html',{'ClostTest':results})

def sentenceFormation(request):
    results = SentenceFormation.objects.all()
    return render(request,'SentenceFormation.html',{'SentenceFormation':results})

def comprehension(request):
    results = Comprehension.objects.all()
    return render(request,'Comprehension.html',{'Comprehension':results})

def orderingWord(request):
    results = OrderingWord.objects.all()
    return render(request,'OrderingWord.html',{'OrderingWord':results})

def oneWordSubstitutes(request):
    results = OneWordSubstitutes.objects.all()
    return render(request,'OneWordSubstitutes.html',{'OneWordSubstitutes':results})

def sentenceCorrection(request):
    results = SentenceCorrection.objects.all()
    return render(request,'SentenceCorrection.html',{'SentenceCorrection':results})

def idiomsPhrases(request):
    results = IdiomsPhrases.objects.all()
    return render(request,'IdiomsPhrases.html',{'IdiomsPhrases':results})

#Engineering Views
def computerScience(request):
    results = ComputerScience.objects.all()
    return render(request,'ComputerScience.html',{'ComputerScience':results})

def chemical(request):
    results = Chemical.objects.all()
    return render(request,'Chemical.html',{'Chemical':results})

def civil(request):
    results = Civil.objects.all()
    return render(request,'Civil.html',{'Civil':results})

def mechanical(request):
    results = Mechanical.objects.all()
    return render(request,'Mechanical.html',{'Mechanical':results})

def structural(request):
    results = Structural.objects.all()
    return render(request,'Structural.html',{'Structural':results})

def electrical(request):
    results = Electrical.objects.all()
    return render(request,'Electrical.html',{'Electrical':results})

#footer link    
def privacyPolicy(request):
    return render(request,'PrivacyPolicy.html')

def tremsConditions(request):
    return render(request,'TremsConditions.html')

def h(request):
    return render(request,'index1.html')