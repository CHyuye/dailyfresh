from django.contrib.auth.decorators import login_required


class LoginRequestMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        # 调用父类的as_view
        view = super(LoginRequestMixin, cls).as_view(**initkwargs)
        return login_required(view)
