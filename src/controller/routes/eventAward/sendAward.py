from discord import Client, TextChannel, Guild, Member, Message
from pymysql import Connection
from src.model.eventAwardManagement import deletAward, newAward
from src.model.userManagement import getUser, addMoneyToUser
from src.model.cashFlowManagement import addNewCashFlow
from src.model.luckyMoneyManagement import newLuckyMoney
from src.utils.readConfig import getLanguageConfig, getMajorConfig

def sendAward(self: Client, message: Message, db: Connection, money: int, userID: int):
    languageConfig = getLanguageConfig()
    majorCOnfig = getMajorConfig()
    uuid = newAward()
    myGuild: Guild = self.guilds[0]
    user: Member = await myGuild.fetch_member(userID)

    if deletAward(db, uuid):
        msg = languageConfig['eventAward']['closeEvent'] \
            .replace('?@user', user.display_name)
        await message.channel.send(msg)
        return
    return